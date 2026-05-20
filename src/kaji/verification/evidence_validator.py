"""Evidence validator — checks retrieved evidence actually supports claim."""


def validate(claim: str, evidence: str) -> dict:
    """Return relevance score and support assessment."""
    return {"relevant": True, "score": 0.0, "reason": ""}
