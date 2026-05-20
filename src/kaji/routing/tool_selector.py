"""Tool selector — injects context-relevant tools based on domain profile."""


def select_tools(profile_config: dict) -> list[str]:
    """Return list of allowed tool names for given profile config."""
    return profile_config.get("tools", ["tavily", "serper"])
