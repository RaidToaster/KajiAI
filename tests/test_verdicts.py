"""Tests for verdict engine."""


from kaji.verdict.labels import ALL_LABELS


def test_all_labels_defined():
    assert len(ALL_LABELS) == 8
    assert "UNVERIFIED" in ALL_LABELS
