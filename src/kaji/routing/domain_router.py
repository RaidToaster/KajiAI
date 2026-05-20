"""Domain router — maps classified claim to appropriate profile."""


from kaji.crews.profile_loader import ProfileLoader


def route(classification: dict, loader: ProfileLoader) -> tuple[str, dict]:
    """Return (profile_name, profile_config) for the classified claim."""
    domain = classification.get("domain", "general")
    return domain, loader.get_profile(domain)
