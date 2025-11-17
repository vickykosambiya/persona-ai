import json
import jsonschema
from schemas.persona_schema import PERSONA_SCHEMA
from utils.llm import call_groq_json

def validate_personas(personas):
    try:
        jsonschema.validate(personas, PERSONA_SCHEMA)
        return personas
    except Exception as e:
        repaired = call_groq_json(
            "You fix persona JSON to match schema.",
            f"ERROR: {e}\n\nDATA:\n{personas}"
        )
        return repaired
