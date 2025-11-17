from typing import Any, Dict
from utils.llm import call_groq_json

def generate_synthetic_customers(
    brand_brief: str,
    constraints: Dict[str, Any],
    n_customers: int = 30,
) -> Dict[str, Any]:

    system_prompt = f"""
You are a market research simulation engine.

Generate statistically PLAUSIBLE synthetic customers.
NO fictional nonsense.

Output STRICT JSON structure:

{{
  "customers": [
    {{
      "id": "cust_1",
      "age": 25,
      "gender": "female",
      "location": "Mumbai, India",
      "income_range": "30k–60k INR",
      "occupation": "Junior executive",
      "interests": ["Instagram", "skincare"],
      "values": ["appearance"],
      "pain_points": ["oily skin"],
      "buying_triggers": ["discounts"],
      "preferred_channels": ["Instagram"]
    }}
  ]
}}

MUST generate exactly {n_customers} customers.
"""

    user_prompt = f"""
Brand:
{brand_brief}

HARD constraints:
{constraints}
"""

    data = call_groq_json(system_prompt, user_prompt)

    if "customers" not in data:
        raise ValueError("Groq did NOT return `customers` field")

    return data
