"""Tests for claim classification."""


from kaji.routing.classifier import classify


def test_classify_returns_dict():
    result = classify("test claim")
    assert isinstance(result, dict)
    assert "domain" in result
