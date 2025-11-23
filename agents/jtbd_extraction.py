from .utils import query_groq, parse_json_output

def jtbd_extraction_agent(persona):
    """
    Extracts the "Functional Job" (Task) and "Emotional Job" (Feeling) for a persona.
    """
    prompt = f"""
    You are the JTBD Extraction Agent (The Psychologist). Analyze the persona and extract the Jobs To Be Done.
    
    Persona:
    {persona}
    
    Identify:
    1. Functional Job: The practical task they want to accomplish.
    2. Emotional Job: How they want to feel or be perceived.
    
    Return JSON:
    {{
        "functional_job": "<string>",
        "emotional_job": "<string>"
    }}
    """
    
    response = query_groq(prompt, json_mode=True)
    return parse_json_output(response)
