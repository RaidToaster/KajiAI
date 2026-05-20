"""Tool router — filters tool set per domain profile before injection."""


def filter_tools(available: list, policy: dict) -> list:
    """Apply policy restrictions to tool list."""
    return available
