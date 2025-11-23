from .utils import query_groq, parse_json_output
import pandas as pd
import io

def synthetic_cluster_agent(validator_output, product_interpreter_output):
    """
    If "Low Data" is flagged, generates synthetic lookalike users to fill the gaps.
    """
    if not validator_output.get("low_data_mode", False):
        return validator_output.get("dataframe")
    
    # Generate synthetic data
    # prompt = f"""
    # You are the Synthetic Cluster Agent. The user has provided insufficient data, so you must generate synthetic user data based on the product context.
    
    # Product Context:
    # {product_interpreter_output}
    
    # Generate 50 rows of synthetic user data that represents potential customers for this product.
    # The data should include columns relevant to segmentation such as:
    # - Age
    # - Job Title
    # - Industry
    # - Pain Points
    # - Goals
    # - Location
    
    # Return the data as a JSON list of objects.
    # """
    prompt = f"""
You are the Synthetic Cluster Agent.

The user uploaded insufficient data, so generate synthetic users that match the product’s likely audience.

Use the product context to infer:
- whether the product is B2B or B2C,
- typical buyer demographics,
- their pain points, goals, motivations,
- relevant industries or lifestyle segments,
- realistic income levels or company revenue ranges.

Product Context:
{product_interpreter_output}

Generate EXACTLY 50 rows of synthetic user data.

Each row must include:
- age
- role_or_job_title (consumer roles for B2C, job titles for B2B)
- industry (use “Consumer” for B2C)
- location
- income (for B2C)
- company_revenue (for B2B; use null for B2C)
- pain_points
- goals
- purchase_motivation
- budget_range (Low, Medium, High)
- experience_level_with_category (Beginner, Intermediate, Advanced)

Rules:
1. Automatically adapt to ANY product category.
2. For B2C: income must be realistic for the persona role and geography.
3. For B2B: company_revenue must reflect realistic business sizes.
4. Ensure diversity across age, income/revenue, and motivations.
5. All outputs must be believable and consistent with the product context.
6. Understand the pain points for the users of given product context.

Return ONLY a JSON list of 50 objects.
"""



    
    response = query_groq(prompt, json_mode=True)
    data = parse_json_output(response)
    
    if isinstance(data, dict) and 'users' in data:
        data = data['users']
    elif isinstance(data, dict):
        # Try to find a list in the dict
        for key, value in data.items():
            if isinstance(value, list):
                data = value
                break
                
    if not isinstance(data, list):
        # Fallback if structure is unexpected
        return pd.DataFrame()
        
    return pd.DataFrame(data)
