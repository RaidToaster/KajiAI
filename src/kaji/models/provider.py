"""LLM provider abstraction — unified interface for multiple providers."""


from crewai import LLM


def create_llm(model_config: dict) -> LLM:
    """Create crewai.LLM instance from config dict.

    Config format: {"provider": "openai", "model": "gpt-4o", ...}
    """
    provider = model_config.get("provider", "openai")
    model = model_config.get("model", "gpt-4o")
    return LLM(
        model=f"{provider}/{model}",
        temperature=model_config.get("temperature", 0.3),
        max_tokens=model_config.get("max_tokens", 4000),
    )
