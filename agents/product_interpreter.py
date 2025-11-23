from .utils import query_groq, parse_json_output

def product_interpreter_agent(product_name, description, category):
    # prompt = f"""
    # You are the Product Interpreter Agent. Your goal is to convert marketing fluff into structured "Value Vectors". By Reading the product name, description, and category, you should be able to extract the core problem the product solves, the specific solution provided, and how it works (the mechanism of action).
    
    # Product Name: {product_name}
    # Category: {category}
    # Description: {description}
    
    # Analyze the input and extract the following in JSON format:
    # {{
    #     "product_name": "{product_name}",
    #     "category": "{category}",
    #     "description": "{description}",
    #     "problem": "The core problem the product solves.",
    #     "solution": "The specific solution provided",
    #     "mechanism": "How it works (the mechanism of action)",
    # }}
    
    # Return ONLY the JSON.
    # """

    prompt = f"""
        You are the Product Interpreter Agent.

        Your job is to read the product name, description, and category, remove all marketing fluff, and convert the information into a clean "Value Vector".

        A Value Vector has 3 parts:
        1. problem: The core problem the product solves (must be 1–2 sentences)
        2. solution: The specific solution the product provides (1–2 sentences)
        3. mechanism: How the product works or achieves its results (1–2 sentences)

        Return the output ONLY in valid JSON. No extra text.

        Input:
        - Product Name: "{product_name}"
        - Category: "{category}"
        - Description: "{description}"

        Output JSON structure:
        {{
            "product_name": "{product_name}",
            "category": "{category}",
            "description": "{description}",
            "problem": "The core problem the product solves.",
            "solution": "The specific solution provided",
            "mechanism": "How it works (the mechanism of action)"
        }}
        """

    
    response = query_groq(prompt, json_mode=True)
    return parse_json_output(response)
