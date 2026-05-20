from dataclasses import dataclass, field
from typing import Any


@dataclass
class ExecutionContext:
    claim: str
    domain: str = "general"
    profile_name: str = "general"
    profile_config: dict[str, Any] = field(default_factory=dict)
    policy: dict[str, Any] = field(default_factory=dict)
    model_config: dict[str, Any] = field(default_factory=dict)
    atomic_claims: list[str] = field(default_factory=list)
    evidence: dict[str, Any] = field(default_factory=dict)
    sources: list[dict[str, Any]] = field(default_factory=list)
    verdicts: list[dict[str, Any]] = field(default_factory=list)
    contradictions: list[dict[str, Any]] = field(default_factory=list)
    execution_id: str = ""
    token_usage: int = 0
    cost_usd: float = 0.0
