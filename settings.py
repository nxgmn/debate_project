GLOBAL_SETTINGS = {
    "temperature": 0.7,
    "formality": "neutral",
    "argument_length": "medium",
}

MODEL_OVERRIDES = {
    "openai": {},
    "gemini": {"temperature": 1.0},  # Example override
    "claude": {"formality": "formal"},
}

def get_model_settings(model_name):
    """Merges global settings with model-specific overrides."""
    settings = GLOBAL_SETTINGS.copy()
    settings.update(MODEL_OVERRIDES.get(model_name, {}))
    return settings

