"""Evidence cache — persist and retrieve evidence results."""


class EvidenceCache:
    def __init__(self):
        self._store: dict[str, dict] = {}

    def get(self, key: str) -> dict | None:
        return self._store.get(key)

    def set(self, key: str, value: dict) -> None:
        self._store[key] = value

    def clear(self) -> None:
        self._store.clear()
