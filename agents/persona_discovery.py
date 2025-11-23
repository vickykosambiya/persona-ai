from .utils import query_groq, parse_json_output
import pandas as pd

def persona_discovery_agent(user_data, product_context, business_goal, anti_personality, geography):
    """
    Segments users into 1 Primary (Cash Cow), 2 Growth, and 1 Negative persona.
    """
    # Convert a sample of user data to string for the prompt to avoid token limits
    data_sample = user_data.head(20).to_string() if not user_data.empty else "No user data available."
    
    prompt = f"""
You are the Persona Discovery Agent.

Your job is to segment the audience into 4 DISTINCT personas using:
- Product Context
- User Data Sample
- Primary Business Goal
- Brand Anti-Personality (who the brand refuses to be)
- Target Geography

-------------------------------------
Product Context:
{product_context}

User Data Sample (20 rows):
{data_sample}

Primary Business Goal:
{business_goal}

Brand Anti-Personality:
{anti_personality}

Target Geography:
{geography}
-------------------------------------

### Your mission:
Identify 4 personas aligned with the business goal and brand positioning:

1. **Cash Cow (Primary)** — Best long-term profitability or goal alignment.
2. **Growth A** — Large audience, easy to acquire.
3. **Growth B** — Niche but valuable segment.
4. **Negative Persona** — Least aligned with BOTH:
   - Business goal
   - Brand anti-personality (explicit misfit)

-------------------------------------
### Rules:
- **Real Names**: Give each persona a REALISTIC full name (e.g., "John May", "Rohan Pandey") based on their demographics and the Target Geography ({geography}).
- **Persona Info**: Provide a short, descriptive title (e.g., "Smart Studios student", "Enterprise CTO").
- **Demographics**: Must include Age Range, Income, Location (must be within {geography}), and Occupation.
- **Negative Persona**: Keep the same structure but focus on why they are a bad fit.
- Personas must not overlap.
- The Negative Persona MUST reflect the Anti-Personality traits.
- Cash Cow must align most with the business goal.
- All personas must be distinct in motivations, behavior, and mindset.
- No generic descriptions or clichés.
- Ground everything in product reality.

-------------------------------------
### Output Format:

Return ONLY valid JSON:
{{
  "cash_cow": {{
    "real_name": "Full Name",
    "persona_info": "Short Title/Description",
    "demographics": {{
      "age_range": "",
      "income": "",
      "location": "",
      "occupation": ""
    }},
    "psychographics": {{
      "goals": "",
      "pain_points": ""
    }},
    "behavioral_traits": "",
    "alignment_with_business_goal": ""
  }},
  "growth_a": {{
    "real_name": "Full Name",
    "persona_info": "Short Title/Description",
    "demographics": {{
      "age_range": "",
      "income": "",
      "location": "",
      "occupation": ""
    }},
    "psychographics": {{
      "goals": "",
      "pain_points": ""
    }},
    "behavioral_traits": "",
    "alignment_with_business_goal": ""
  }},
  "growth_b": {{
    "real_name": "Full Name",
    "persona_info": "Short Title/Description",
    "demographics": {{
      "age_range": "",
      "income": "",
      "location": "",
      "occupation": ""
    }},
    "psychographics": {{
      "goals": "",
      "pain_points": ""
    }},
    "behavioral_traits": "",
    "alignment_with_business_goal": ""
  }},
  "negative_persona": {{
    "real_name": "Full Name",
    "persona_info": "Short Title/Description",
    "demographics": {{
      "age_range": "",
      "income": "",
      "location": "",
      "occupation": ""
    }},
    "psychographics": {{
      "why_they_wont_buy": "",
      "misalignment_reason": "Explain how they conflict with the anti-personality"
    }},
    "behavioral_traits": ""
  }}
}}
"""

    
    response = query_groq(prompt, json_mode=True)
    return parse_json_output(response)
