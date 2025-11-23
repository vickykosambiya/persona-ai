from .utils import query_groq, parse_json_output

def offer_strategy_agent(primary_goal, objection, persona_name):
    """
    Creates a pricing bundle specifically designed to overcome the persona's main objection.
    """
    prompt = f"""
    You are the Offer Strategy Agent (The Closer). Create an irresistible offer.
    
    Business Goal: {primary_goal}
    Main Objection: {objection}
    Persona: {persona_name}
    
    Create a "Pricing Bundle" or "Offer Structure" that neutralizes the objection and achieves the goal.
    
    Return JSON:
    {{
        "offer_name": "<string>",
        "price_point_strategy": "<string>",
        "included_items": ["<item1>", "<item2>", ...],
        "objection_handling": "<how this offer fixes the objection>"
    }}
    """
    
    response = query_groq(prompt, json_mode=True)
    return parse_json_output(response)
