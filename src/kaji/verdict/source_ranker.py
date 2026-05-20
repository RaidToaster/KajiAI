"""Source ranker — ranks sources by composite credibility score."""


def rank(sources: list[dict]) -> list[dict]:
    """Sort sources by credibility_score descending. Return sorted list."""
    return sorted(sources, key=lambda s: s.get("credibility_score", 0), reverse=True)
