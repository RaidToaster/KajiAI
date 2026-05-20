from crewai import Agent, Crew, Process, Task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import Any

from kaji.crews.profile_loader import ProfileLoader
from kaji.crews.execution_context import ExecutionContext


class BaseVerificationCrew:
    def __init__(self, ctx: ExecutionContext, loader: ProfileLoader):
        self.ctx = ctx
        self.loader = loader
        self._agents: list[BaseAgent] | None = None
        self._tasks: list[Task] | None = None

    def _build_agent(self, role_key: str) -> Agent:
        config = self.loader.agents[role_key]
        profile = self.ctx.profile_config
        llm_config = self.ctx.model_config

        allowed_tools = profile.get("tools", [])
        agent_tools = self._resolve_tools(allowed_tools)

        return Agent(
            role=config["role"],
            goal=config["goal"],
            backstory=config["backstory"],
            tools=agent_tools,
            verbose=True,
            llm=f"{llm_config['provider']}/{llm_config['model']}",
        )

    def _build_task(self, task_key: str, agent: BaseAgent) -> Task:
        config = self.loader.tasks[task_key]
        return Task(
            description=config["description"],
            expected_output=config["expected_output"],
            agent=agent,
        )

    def _resolve_tools(self, tool_names: list[str]) -> list:
        tools = []
        for name in tool_names:
            tool = self._instantiate_tool(name)
            if tool:
                tools.append(tool)
        return tools

    def _instantiate_tool(self, name: str):
        try:
            mod = __import__(f"kaji.tools.{name}", fromlist=["tool"])
            return getattr(mod, "tool", None) or getattr(mod, name, None)()
        except (ImportError, AttributeError):
            return None

    @property
    def agents(self) -> list[BaseAgent]:
        if self._agents is None:
            agent_names = self.ctx.profile_config.get(
                "agents",
                ["lead_researcher", "fact_checker", "source_analyst", "contradiction_analyst", "synthesis_writer"],
            )
            self._agents = [self._build_agent(name) for name in agent_names]
        return self._agents

    @property
    def tasks(self) -> list[Task]:
        if self._tasks is None:
            task_map = {
                "lead_researcher": ["decompose_task", "research_task"],
                "fact_checker": ["fact_check_task"],
                "source_analyst": ["source_analysis_task"],
                "contradiction_analyst": ["contradiction_task"],
                "synthesis_writer": ["synthesis_task"],
            }
            agent_names = self.ctx.profile_config.get(
                "agents",
                ["lead_researcher", "fact_checker", "source_analyst", "contradiction_analyst", "synthesis_writer"],
            )
            tasks = []
            for name in agent_names:
                agent = self._build_agent(name)
                for task_key in task_map.get(name, []):
                    tasks.append(self._build_task(task_key, agent))
            self._tasks = tasks
        return self._tasks

    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
