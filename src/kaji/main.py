#!/usr/bin/env python
import sys
import json
import warnings

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

from kaji.flow import KajiFlow


def run():
    inputs = {
        "claim": "The moon landing was faked.",
        "domain": "general",
    }
    result = KajiFlow().kickoff(inputs=inputs)
    if hasattr(result, "raw"):
        print(result.raw)
    else:
        print(result)


def run_with_inputs(claim: str, domain: str = "general"):
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
        raise Exception("No trigger payload provided. Please provide JSON payload as argument.")
    try:
        trigger_payload = json.loads(sys.argv[1])
    except json.JSONDecodeError:
        raise Exception("Invalid JSON payload provided as argument")

    claim = trigger_payload.get("claim", "")
    domain = trigger_payload.get("domain", "general")

    result = KajiFlow().kickoff(inputs={"claim": claim, "domain": domain})
    return result
