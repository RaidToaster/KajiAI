import yaml
from pathlib import Path
from typing import Any


def load_yaml(path: Path) -> dict[str, Any]:
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


class ProfileLoader:
    def __init__(self, config_dir: Path):
        self.config_dir = config_dir
        self._profiles: dict[str, Any] | None = None
        self._policies: dict[str, Any] | None = None
        self._agents: dict[str, Any] | None = None
        self._tasks: dict[str, Any] | None = None
        self._models: dict[str, Any] | None = None

    @property
    def profiles(self) -> dict[str, Any]:
        if self._profiles is None:
            self._profiles = load_yaml(self.config_dir / "profiles.yaml")
        return self._profiles

    @property
    def policies(self) -> dict[str, Any]:
        if self._policies is None:
            raw = load_yaml(self.config_dir / "policies.yaml")
            self._policies = self._resolve_inheritance(raw)
        return self._policies

    @property
    def agents(self) -> dict[str, Any]:
        if self._agents is None:
            self._agents = load_yaml(self.config_dir / "agents.yaml")
        return self._agents

    @property
    def tasks(self) -> dict[str, Any]:
        if self._tasks is None:
            self._tasks = load_yaml(self.config_dir / "tasks.yaml")
        return self._tasks

    @property
    def models(self) -> dict[str, Any]:
        if self._models is None:
            self._models = load_yaml(self.config_dir / "models.yaml")
        return self._models

    def get_profile(self, name: str) -> dict[str, Any]:
        return self.profiles.get(name, self.profiles["general"])

    def get_policy(self, profile: str) -> dict[str, Any]:
        return self.policies.get(profile, self.policies["default"])

    @staticmethod
    def _resolve_inheritance(raw: dict) -> dict:
        resolved = {}
        for key, val in raw.items():
            if isinstance(val, dict) and "inherit" in val:
                parent = resolved.get(val["inherit"], raw.get(val["inherit"], {}))
                merged = {**parent, **{k: v for k, v in val.items() if k != "inherit"}}
                resolved[key] = merged
            else:
                resolved[key] = val
        return resolved
