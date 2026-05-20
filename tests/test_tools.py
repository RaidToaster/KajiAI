"""Tests for tool layer."""


def test_tool_imports():
    from kaji.tools.custom_tool import CustomTool
    tool = CustomTool()
    assert tool.name == "custom_tool"
