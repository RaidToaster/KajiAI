"""Search cache — caches search results to avoid duplicate API calls."""


class SearchCache:
    def __init__(self):
        self._store: dict[str, list[dict]] = {}

    def get(self, query: str) -> list[dict] | None:
        return self._store.get(query)

    def set(self, query: str, results: list[dict]) -> None:
        self._store[query] = results
