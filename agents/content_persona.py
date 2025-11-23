from .utils import query_groq, parse_json_output

def content_persona_agent(jtbd, brand_voice, persona_demographics):
    """
    Generates 3 hook styles and 1 meme concept matching the brand voice.
    """
    prompt = f"""
You are the Content Persona Agent (The Copywriter). 
Your job is to generate high-converting creative ideas tailored to the persona’s psychology and the brand's tone.

------------------------------------
JTBD (Jobs To Be Done):
{jtbd}

Brand Voice (Tone/Personality):
{brand_voice}

Persona Context (Demographics + Psychographics):
{persona_demographics}
------------------------------------

### Create:
1. **Three high-impact hooks**  
   - Must be scroll-stopping  
   - Must directly speak to the persona’s emotional and functional JTBD  
   - Must reflect the Brand Voice  
   - Should feel platform-ready (Instagram/TikTok/LinkedIn depending on persona)  
   - No generic clichés, no fluff  

2. **One Meme Concept**  
   - Describe the visual setup (simple + easy to design)  
   - Add the caption using the Brand Voice  
   - Should reflect the persona’s pain point or desire  
   - Must be actually funny, relatable, or insightful  

------------------------------------
### Output JSON (MANDATORY):

{{
  "hooks": [
    "<hook1>",
    "<hook2>",
    "<hook3>"
  ],
  "meme_concept": {{
    "visual": "<visual_description>",
    "caption": "<caption_text>"
  }}
}}
------------------------------------

Return ONLY valid JSON.
"""

    
    response = query_groq(prompt, json_mode=True)
    return parse_json_output(response)
