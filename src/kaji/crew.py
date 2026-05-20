from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent


@CrewBase
class Kaji:
    """Kaji crew — entry point for crewAI CLI integration."""

    agents: list[BaseAgent] = []
    tasks: list[Task] = []

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def lead_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config["lead_researcher"],  # type: ignore[index]
            verbose=True,
        )

    @agent
    def fact_checker(self) -> Agent:
        return Agent(
            config=self.agents_config["fact_checker"],  # type: ignore[index]
            verbose=True,
        )

    @agent
    def source_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config["source_analyst"],  # type: ignore[index]
            verbose=True,
        )

    @agent
    def contradiction_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config["contradiction_analyst"],  # type: ignore[index]
            verbose=True,
        )

    @agent
    def synthesis_writer(self) -> Agent:
        return Agent(
            config=self.agents_config["synthesis_writer"],  # type: ignore[index]
            verbose=True,
        )

    @task
    def decompose_task(self) -> Task:
        return Task(
            config=self.tasks_config["decompose_task"],  # type: ignore[index]
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config["research_task"],  # type: ignore[index]
        )

    @task
    def fact_check_task(self) -> Task:
        return Task(
            config=self.tasks_config["fact_check_task"],  # type: ignore[index]
        )

    @task
    def source_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config["source_analysis_task"],  # type: ignore[index]
        )

    @task
    def contradiction_task(self) -> Task:
        return Task(
            config=self.tasks_config["contradiction_task"],  # type: ignore[index]
        )

    @task
    def synthesis_task(self) -> Task:
        return Task(
            config=self.tasks_config["synthesis_task"],  # type: ignore[index]
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
