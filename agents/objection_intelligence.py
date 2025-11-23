from .utils import query_groq, parse_json_output

def objection_intelligence_agent(jtbd, anti_personality):
    """
    Predicts the specific reason this persona will say "NO" (Price, Trust, Timing).
    """
    prompt = f"""
    You are the Objection Intelligence Agent (The Skeptic). Predict why the persona will say NO.
    
    JTBD: {jtbd}
    Anti-Personality (Who we are NOT): {anti_personality}
    
    Identify the main objection categories:
    1. Price
    2. Trust
    3. Timing
    4. Product Fit
    
    Select the PRIMARY objection and explain why.
    
    Return JSON:
    {{
        "primary_objection": "<string>",
        "reasoning": "<string>",
        "mitigation_strategy": "<string>"
    }}
    """
    
    response = query_groq(prompt, json_mode=True)
    return parse_json_output(response)
