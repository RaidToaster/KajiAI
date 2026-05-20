#!/usr/bin/env python
import sys
import json
import warnings

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

from crewai import Agent, LLM


def run():
    llm = LLM(
        model="ollama/gemma4",
        base_url="http://localhost:11434",
    )
    agent = Agent(
        role="Connectivity Tester",
        goal="Respond to the user's message to confirm the LLM connection works.",
        backstory="You are a helpful assistant that gives short, direct answers.",
        llm=llm,
        verbose=True,
    )
    result = agent.kickoff(
        "Respond with exactly: 'Ollama OK. Model: gemma4' followed by a one-sentence greeting."
    )
    print("\n--- RESULT ---")
    print(result.raw)
    print("--- END ---")


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
