from utils.llm import call_groq_json
from typing import Dict, Any

def extract_insights_and_segments(synthetic_data: Dict[str, Any], max_segments: int = 5):
    system_prompt = """
You are a segmentation engine.
Cluster customers logically based on behaviors & demographics.

STRICT JSON structure:

{
 "segments": [
   {
     "id": "seg_1",
     "name": "Urban Minimalists",
     "summary": "Young metro skincare buyers",
     "representative_customers": ["cust_3","cust_8"],
     "shared_traits": ["acne prone", "instagram shoppers"]
   }
 ]
}
"""
    user_prompt = f"""
Here is customer JSON:

{synthetic_data}

Max segments = {max_segments}
"""

    return call_groq_json(system_prompt, user_prompt)
