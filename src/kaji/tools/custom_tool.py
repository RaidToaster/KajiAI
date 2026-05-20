"""Custom tool template — replace with actual tool implementations."""


from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field


class CustomToolInput(BaseModel):
    query: str = Field(..., description="Search query")


class CustomTool(BaseTool):
    name: str = "custom_tool"
    description: str = "Custom tool — replace with actual implementation."
    args_schema: Type[BaseModel] = CustomToolInput

    def _run(self, query: str) -> str:
        return f"Stub result for: {query}"
