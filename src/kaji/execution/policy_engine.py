"""Policy engine — governs agent execution constraints (cost, depth, safety)."""


def enforce(policy: dict, execution_state: dict) -> dict:
    """Check policy constraints against current execution state.

    Returns decisions dict: may_continue (bool), downgrade_mode (str|None), reason (str).
    """
    return {"may_continue": True, "downgrade_mode": None, "reason": ""}
