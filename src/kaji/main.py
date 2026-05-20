#!/usr/bin/env python
import sys
import json
import warnings

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

from kaji.crews.fact_check_crew import run as fact_check


def run():
    import sys

    if len(sys.argv) > 1:
        claim = " ".join(sys.argv[1:])
    else:
        claim = input("Enter a claim to fact-check: ").strip()

    if not claim:
        print("No claim entered. Exiting.")
        return

    print(f"\n{'='*60}")
    print(f"  KajiSF-DJ Fact Check")
    print(f"{'='*60}")
    print(f"  Claim: {claim}")
    print(f"{'='*60}\n")

    result = fact_check(claim)

    print(f"\n{'='*60}")
    print("  RESULT")
    print(f"{'='*60}")
    print(result)
    print(f"{'='*60}")


def demo():
    claim = "Vaccines cause autism"
    print(f"Running demo with claim: {claim}\n")
    result = fact_check(claim)
    print(result)


def run_with_inputs(claim: str, domain: str = "general"):
    from kaji.flow import KajiFlow
    flow = KajiFlow()
    result = flow.kickoff(inputs={"claim": claim, "domain": domain})
    return result


def train():
    from kaji.crew import Kaji
    if len(sys.argv) < 3:
        print("Usage: crewai train <n_iterations> <filename>")
        sys.exit(1)
    Kaji().crew().train(
        n_iterations=int(sys.argv[1]),
        filename=sys.argv[2],
        inputs={"claim": "Test claim for training", "domain": "general", "current_year": "2026"},
    )


def replay():
    from kaji.crew import Kaji
    if len(sys.argv) < 2:
        print("Usage: crewai replay <task_id>")
        sys.exit(1)
    Kaji().crew().replay(task_id=sys.argv[1])


def test():
    from kaji.crew import Kaji
    if len(sys.argv) < 3:
        print("Usage: crewai test <n_iterations> <eval_llm>")
        sys.exit(1)
    Kaji().crew().test(
        n_iterations=int(sys.argv[1]),
        eval_llm=sys.argv[2],
        inputs={"claim": "Test claim", "domain": "general", "current_year": "2026"},
    )


def run_with_trigger():
    if len(sys.argv) < 2:
        raise Exception("No trigger payload provided.")
    try:
        trigger_payload = json.loads(sys.argv[1])
    except json.JSONDecodeError:
        raise Exception("Invalid JSON payload")

    claim = trigger_payload.get("claim", "")
    domain = trigger_payload.get("domain", "general")

    from kaji.flow import KajiFlow
    result = KajiFlow().kickoff(inputs={"claim": claim, "domain": domain})
    return result
