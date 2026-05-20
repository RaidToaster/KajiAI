from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field


class DuckDuckGoSearchInput(BaseModel):
    query: str = Field(..., description="Search query string")


class DuckDuckGoSearchTool(BaseTool):
    name: str = "web_search"
    description: str = "Search the web using DuckDuckGo. Use this to find current information about claims, news, and facts."
    args_schema: Type[BaseModel] = DuckDuckGoSearchInput

    def _run(self, query: str) -> str:
        from ddgs import DDGS

        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=5))

        if not results:
            return "No search results found."

        lines = []
        for i, r in enumerate(results, 1):
            title = r.get("title", "")
            body = r.get("body", "")
            href = r.get("href", "")
            lines.append(f"{i}. {title}\n   {body}\n   URL: {href}")
        return "\n\n".join(lines)


def tool():
    return DuckDuckGoSearchTool()
