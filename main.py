import json
from pipelines.build_personas import build_personas_pipeline

brand_brief = """
We are a science-backed acne friendly skincare brand targeting Gen-Z India.
"""

constraints = {
 "age_range": "18-30",
 "region": "India Tier 1-2",
 "income": "25k-60k INR"
}

personas = build_personas_pipeline(brand_brief, constraints)

print(json.dumps(personas, indent=2, ensure_ascii=False))
