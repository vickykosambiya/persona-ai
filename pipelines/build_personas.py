from agents.synthetic_generator import generate_synthetic_customers
from agents.insight_agent import extract_insights_and_segments
from agents.persona_writer import build_personas_from_segments
from agents.validator import validate_personas

def build_personas_pipeline(brand_brief: str, constraints: dict):

    synthetic = generate_synthetic_customers(brand_brief, constraints, n_customers=40)

    segments = extract_insights_and_segments(synthetic)

    personas = build_personas_from_segments(segments, brand_brief)

    final_personas = validate_personas(personas)

    return final_personas
