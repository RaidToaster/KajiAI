"""Retry controller — handles transient failures with fallback and backoff."""


import asyncio


class RetryController:
    def __init__(self, max_retries: int = 3, delay: float = 2.0):
        self.max_retries = max_retries
        self.delay = delay

    async def execute(self, fn, *args, **kwargs):
        last_exc = None
        for attempt in range(self.max_retries):
            try:
                return await fn(*args, **kwargs)
            except Exception as e:
                last_exc = e
                if attempt < self.max_retries - 1:
                    await asyncio.sleep(self.delay * (attempt + 1))
        raise last_exc
