from .utils import query_groq, parse_json_output

def channel_affinity_agent(geography, category, persona_demographics):
    """
    Predicts the highest ROI platforms (e.g., LinkedIn vs. TikTok) for each persona.
    """
    prompt = f"""
You are the Channel Affinity Agent (The Media Planner). 
Your job is to recommend the top 3 marketing channels with the highest predicted ROI for this persona, based on:

- Target Geography
- Market Category
- Persona Demographics (age, job/role, behavior clues)

------------------------------
Geography: {geography}
Category: {category}
Persona Demographics:
{persona_demographics}
------------------------------

### Rules for Channel Selection:

1. **Match Platform Behavior to Persona Type**
   - Younger audiences → TikTok, Instagram, YouTube
   - Professionals → LinkedIn, Email, Webinars
   - Parents → Facebook, Pinterest
   - High-income → Instagram, YouTube, LinkedIn
   - Niche interests → Reddit, Discord, Niche forums

2. **Match Category to Channel Strength**
   - Beauty/Fashion → Instagram, TikTok, YouTube
   - SaaS/B2B → LinkedIn, Google Search, Email, Webinars
   - Consumer Goods → Instagram, Facebook, YouTube
   - Education → YouTube, LinkedIn, Google Search
   - Luxury → Instagram, YouTube, Influencers
   - Tech/AI → YouTube, Reddit, LinkedIn, Twitter

3. **Match Geography**
   - India → Instagram, YouTube, WhatsApp, Facebook
   - US/UK → Instagram, TikTok, YouTube, LinkedIn
   - Middle East → Instagram, Snapchat, YouTube
   - SEA → Facebook, TikTok, YouTube
   - EU → Instagram, YouTube, LinkedIn

4. **Audience Fit**
   - Channels must reflect the persona’s digital maturity and content consumption patterns.

5. **ROI Score**
   - ROI score = 1–10 based on expected effectiveness.

------------------------------
### Output (MANDATORY JSON):

{{
  "channels": [
    {{
      "name": "",
      "roi_score": 0,
      "rationale": ""
    }},
    {{
      "name": "",
      "roi_score": 0,
      "rationale": ""
    }},
    {{
      "name": "",
      "roi_score": 0,
      "rationale": ""
    }}
  ]
}}
------------------------------

Return ONLY valid JSON.
"""

    
    response = query_groq(prompt, json_mode=True)
    return parse_json_output(response)
