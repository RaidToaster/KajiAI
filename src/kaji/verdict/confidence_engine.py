"""Confidence engine — multi-factor confidence scoring."""


WEIGHTS = {
    "source_independence": 0.25,
    "evidence_specificity": 0.25,
    "internal_consistency": 0.20,
    "contradiction_severity": 0.15,
    "source_credibility": 0.10,
    "temporal_freshness": 0.03,
    "evidence_quantity": 0.02,
}


def compute(factors: dict) -> float:
    """Compute weighted confidence score from factor dict."""
    score = 0.0
    for key, weight in WEIGHTS.items():
        score += factors.get(key, 0.0) * weight
    return round(score, 2)
