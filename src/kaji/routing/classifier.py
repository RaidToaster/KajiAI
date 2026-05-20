"""Claim classifier — determines category, domain, risk, and complexity."""


def classify(claim: str) -> dict:
    """Classify claim into domain profile and risk level.

    Returns dict with: category, domain, risk_level, complexity, recommended_tools.
    """
    return {
        "category": "general",
        "domain": "general",
        "risk_level": "low",
        "complexity": "simple",
        "recommended_tools": ["tavily", "serper"],
    }
