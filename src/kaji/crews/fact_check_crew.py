from crewai import Agent, Crew, Process, Task
from crewai import LLM

from kaji.tools.duckduckgo import DuckDuckGoSearchTool


def _llm():
    return LLM(
        model="ollama/gemma4",
        base_url="http://localhost:11434",
        temperature=0.3,
    )


def run(claim: str) -> str:
    search_tool = DuckDuckGoSearchTool()

    researcher = Agent(
        role="Fact Check Researcher",
        goal=(
            "Search the web for evidence related to the claim. "
            "Find sources that support AND contradict the claim. "
            "Return raw search results with URLs."
        ),
        backstory=(
            "You are a thorough web researcher who always finds multiple perspectives. "
            "You never make up facts — you only report what search results tell you."
        ),
        tools=[search_tool],
        llm=_llm(),
        verbose=True,
    )

    analyst = Agent(
        role="Fact Check Analyst",
        goal=(
            "Analyze all evidence and produce a clear verdict. "
            "Determine if the claim is TRUE, FALSE, MISLEADING, or UNVERIFIED. "
            "Explain your reasoning and cite sources."
        ),
        backstory=(
            "You are a professional fact-checker who weighs evidence carefully. "
            "You distinguish between strong and weak sources. "
            "You always explain WHY you reached a conclusion."
        ),
        llm=_llm(),
        verbose=True,
    )

    task_research = Task(
        description=(
            f"Search the web for evidence about this claim: '{claim}'\n\n"
            "Find at least 3-5 relevant sources. Look for:\n"
            "- Official sources (government, scientific institutions)\n"
            "- News articles from reputable outlets\n"
            "- Fact-checking sites (Snopes, AFP, Reuters)\n"
            "- Sources that contradict the claim\n\n"
            "Return ALL search results with full URLs."
        ),
        expected_output=(
            "A list of search results with titles, snippets, and URLs. "
            "Include both supporting and contradicting sources."
        ),
        agent=researcher,
    )

    task_analyze = Task(
        description=(
            f"Analyze this claim: '{claim}'\n\n"
            "Based on the search results provided, determine:\n"
            "1. Is there credible evidence supporting the claim?\n"
            "2. Is there credible evidence contradicting the claim?\n"
            "3. What is the overall verdict?\n\n"
            "Verdict options:\n"
            "- TRUE: Strong evidence supports the claim\n"
            "- FALSE: Strong evidence contradicts the claim\n"
            "- MISLEADING: Claim has some truth but is missing context\n"
            "- UNVERIFIED: Not enough reliable evidence\n\n"
            "Format your response as:\n"
            "## Verdict: [TRUE/FALSE/MISLEADING/UNVERIFIED]\n"
            "**Confidence:** [High/Medium/Low]\n\n"
            "**Summary:** [2-3 sentence explanation]\n\n"
            "**Evidence:**\n"
            "- Bullet points with key findings and source URLs\n\n"
            "**Sources:**\n"
            "- List all sources referenced"
        ),
        expected_output=(
            "A structured fact-check report with verdict, confidence, "
            "summary, evidence list, and sources."
        ),
        agent=analyst,
    )

    crew = Crew(
        agents=[researcher, analyst],
        tasks=[task_research, task_analyze],
        process=Process.sequential,
        verbose=True,
    )

    result = crew.kickoff()
    return result.raw
