from utils.llm import call_groq_json
from typing import Dict, Any

def build_personas_from_segments(segments: Dict[str, Any], brand_brief: str):

    system_prompt = """
You are a persona builder.
Convert segments into FINAL personas.

STRICT JSON SCHEMA:

{
 "personas": [
   {
     "id": "persona_1",
     "name": "Skin-savvy Sneha",
     "summary": "Young shopper who wants...",
     "demographics": {
       "age_range": "22-30",
       "gender": "female",
       "location": "Tier 1 India"
     },
     "psychographics": {
       "values": ["appearance"],
       "interests": ["instagram"],
       "personality_traits": ["impulsive"]
     },
     "goals": ["clear skin"],
     "pain_points": ["too many products"],
     "buying_triggers": ["influencers"],
     "channels": ["Instagram"],
     "tone_and_messaging": {
       "tone": "friendly",
       "key_messages": ["backed by science"]
     }
   }
 ]
}
"""

    user_prompt = f"""
Brand:
{brand_brief}

Segments:
{segments}
"""

    personas = call_groq_json(system_prompt, user_prompt)

    if "personas" not in personas:
        raise ValueError("Groq returned NO personas")

    return personas
