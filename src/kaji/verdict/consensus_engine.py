"""Consensus engine — resolves conflicting evidence without averaging confidence."""


def resolve_conflict(verdicts: list[dict]) -> str:
    """Detect epistemic stalemates. Escalate when equally credible sources conflict."""
    labels = [v.get("verdict", "UNVERIFIED") for v in verdicts]
    unique = set(labels)

    if len(unique) > 1 and all(l in ("TRUE", "FALSE") for l in unique):
        return "NEEDS_CONTEXT"
    return max(set(labels), key=labels.count)
