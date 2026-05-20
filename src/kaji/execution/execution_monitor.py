"""Execution monitor — observes agent execution and collects metrics."""


class ExecutionMonitor:
    def __init__(self):
        self.events: list[dict] = []

    def record(self, event: str, data: dict) -> None:
        self.events.append({"event": event, "data": data})

    def summary(self) -> dict:
        return {
            "total_events": len(self.events),
            "events": self.events[-10:],
        }
