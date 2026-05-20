"""Budget manager — tracks token and cost usage, triggers downgrade."""


class BudgetManager:
    def __init__(self, ceiling_usd: float = 0.50):
        self.ceiling_usd = ceiling_usd
        self.total_cost = 0.0
        self.token_usage = 0

    def track(self, cost: float, tokens: int) -> None:
        self.total_cost += cost
        self.token_usage += tokens

    def is_exceeded(self) -> bool:
        return self.total_cost >= self.ceiling_usd
