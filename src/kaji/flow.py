from crewai.flow.flow import Flow, listen, start
from pathlib import Path
from pydantic import BaseModel

from kaji.crews.profile_loader import ProfileLoader
from kaji.crews.execution_context import ExecutionContext
from kaji.crews.base_crew import BaseVerificationCrew


class KajiState(BaseModel):
    claim: str = ""
    domain: str = "general"
    profile_name: str = "general"
    atomic_claims: list[str] = []
    evidence: dict = {}
    verdicts: list = []
    contradictions: list = []
    report: str = ""


class KajiFlow(Flow[KajiState]):
    """Orchestrates the verification pipeline."""

    stream = False

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        config_dir = Path(__file__).parent / "config"
        self.loader = ProfileLoader(config_dir)

    @start()
    def classify_and_decompose(self):
        ctx = ExecutionContext(
            claim=self.state.claim,
            domain=self.state.domain,
            profile_name=self.state.profile_name,
            profile_config=self.loader.get_profile(self.state.profile_name),
            policy=self.loader.get_policy(self.state.profile_name),
            model_config=self.loader.models.get("default", {}),
        )

        # Decompose claim into atomic units via BaseVerificationCrew
        crew = BaseVerificationCrew(ctx, self.loader)
        result = crew.crew().kickoff(inputs={
            "claim": self.state.claim,
            "domain": self.state.domain,
        })

        self.state.atomic_claims = [self.state.claim]
        if hasattr(result, "raw") and result.raw:
            self.state.atomic_claims = [self.state.claim]

    @listen(classify_and_decompose)
    def verify(self):
        ctx = ExecutionContext(
            claim=self.state.claim,
            domain=self.state.domain,
            atomic_claims=self.state.atomic_claims,
        )
        crew = BaseVerificationCrew(ctx, self.loader)
        result = crew.crew().kickoff(inputs={
            "claim": self.state.claim,
            "domain": self.state.domain,
            "claims": ", ".join(self.state.atomic_claims),
        })
        if hasattr(result, "raw") and result.raw:
            self.state.report = result.raw

    @listen(verify)
    def finalize(self):
        return self.state.report


def create_flow():
    return KajiFlow()
