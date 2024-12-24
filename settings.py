# settings.py

# Global settings (default for all models)
global_settings = {
    "temperature": 0.7,
    "formality": "neutral",
    "argument_length": "medium",
}

# Model-specific overrides
model_overrides = {}

# Global settings functions
def get_global_settings():
    """Retrieve global settings."""
    return global_settings

def update_global_setting(key: str, value):
    """Update a global setting."""
    if key in global_settings:
        global_settings[key] = value
        return True
    else:
        raise KeyError(f"Invalid setting key: {key}")

# Model-specific override functions
def get_model_override(model_name: str):
    """Retrieve overrides for a specific model."""
    return model_overrides.get(model_name, {})

def update_model_override(model_name: str, key: str, value):
    """Update or add an override for a specific model."""
    if model_name not in model_overrides:
        model_overrides[model_name] = {}
    model_overrides[model_name][key] = value

def reset_model_override(model_name: str):
    """Clear all overrides for a specific model."""
    if model_name in model_overrides:
        del model_overrides[model_name]

# Helper to get final settings for a model
def get_final_settings(model_name: str):
    """Combine global settings with model-specific overrides."""
    final_settings = global_settings.copy()
    overrides = get_model_override(model_name)
    final_settings.update(overrides)
    return final_settings
