"""Tests for verification layer."""


from kaji.verification.evidence_validator import validate


def test_validate_stub():
    result = validate("test claim", "test evidence")
    assert "relevant" in result
