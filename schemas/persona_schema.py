PERSONA_SCHEMA = {
    "type": "object",
    "properties": {
        "personas": {
            "type": "array",
            "minItems": 1,
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "string"},
                    "name": {"type": "string"},
                    "summary": {"type": "string"},
                    "demographics": {
                        "type": "object",
                        "properties": {
                            "age_range": {"type": "string"},
                            "gender": {"type": ["string", "null"]},
                            "location": {"type": "string"},
                            "income_range": {"type": ["string", "null"]},
                            "occupation": {"type": ["string", "null"]},
                        },
                        "required": ["age_range", "location"],
                    },
                    "psychographics": {
                        "type": "object",
                        "properties": {
                            "values": {"type": "array", "items": {"type": "string"}},
                            "interests": {"type": "array", "items": {"type": "string"}},
                            "personality_traits": {
                                "type": "array",
                                "items": {"type": "string"},
                            },
                        },
                        "required": ["values", "interests"],
                    },
                    "goals": {
                        "type": "array",
                        "items": {"type": "string"},
                    },
                    "pain_points": {
                        "type": "array",
                        "items": {"type": "string"},
                    },
                    "buying_triggers": {
                        "type": "array",
                        "items": {"type": "string"},
                    },
                    "channels": {
                        "type": "array",
                        "items": {"type": "string"},
                    },
                    "tone_and_messaging": {
                        "type": "object",
                        "properties": {
                            "tone": {"type": "string"},
                            "key_messages": {
                                "type": "array",
                                "items": {"type": "string"},
                            },
                        },
                        "required": ["tone", "key_messages"],
                    },
                },
                "required": [
                    "id",
                    "name",
                    "summary",
                    "demographics",
                    "psychographics",
                    "goals",
                    "pain_points",
                    "buying_triggers",
                    "channels",
                    "tone_and_messaging",
                ],
            },
        }
    },
    "required": ["personas"],
}
