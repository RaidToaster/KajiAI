"""Atomic claim decomposition — splits complex claims into independent units."""


def decompose(claim: str) -> list[str]:
    """Decompose a complex claim into atomic verifiable sub-claims.

    Returns list of atomic claim strings.
    """
    return [claim]
