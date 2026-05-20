"""Verdict engine — computes final verdict from sub-verdicts and contradictions."""


def resolve(sub_verdicts: list[dict], contradictions: list[dict]) -> dict:
    """Aggregate sub-verdicts. Return final verdict with confidence."""
    return {
        "verdict": "UNVERIFIED",
        "confidence": 0.0,
        "rationale": "Stub — no evidence processed.",
    }
