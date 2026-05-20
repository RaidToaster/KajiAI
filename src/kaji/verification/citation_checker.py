"""Citation checker — validates URLs exist and were actually retrieved."""


def check(url: str) -> dict:
    """Verify URL accessibility. Returns status and metadata."""
    return {"accessible": False, "status_code": None, "error": "stub"}
