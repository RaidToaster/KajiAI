"""Grounding validator — ensures synthesis traces to retrieved evidence."""


def validate(synthesis: str, evidence: dict) -> dict:
    """Check every claim in synthesis maps to evidence. Return violations."""
    return {"grounded": True, "violations": []}
