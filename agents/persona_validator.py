from .utils import query_groq, parse_json_output

def persona_validator_agent(personas, primary_goal):
    """
    Scores the generated personas against the business goal.
    """
    prompt = f"""
        You are the Persona Validator Agent (The Skeptical Manager).

        Your job:
        Evaluate whether the 4 personas are strategically correct AND aligned with the Primary Business Goal.

        -----------------------------------
        Primary Business Goal:
        {primary_goal}

        Personas (JSON input):
        {personas}
        -----------------------------------

        ### Validation Rules:

        1. **Cash Cow must:**
        - Strongly support the business goal.
        - Have high revenue potential or high adoption probability.
        - Have clear, realistic goals and pain points.

        2. **Growth A must:**
        - Represent a high-volume, easy-to-reach segment.
        - Not overlap with Cash Cow.

        3. **Growth B must:**
        - Represent a niche with clear but narrower value.
        - Be meaningfully different from Growth A.

        4. **Negative Persona must:**
        - Clearly conflict with the business goal.
        - Represent a poor fit segment.
        - Have explicit misalignment reasons.

        5. **General Requirements:**
        - Personas must NOT overlap in demographics, motivations, or buying logic.
        - They must be realistic given the product context.
        - Psychographics must be consistent and non-generic.
        - Behavioral traits must be relevant to purchasing behavior.

        ### Scoring Method:
        Score from 0 to 100 based on:
        - 40% = Alignment with business goal  
        - 30% = Distinctiveness & non-overlap  
        - 20% = Realism & clarity  
        - 10% = Accuracy of Negative Persona  

        Score Interpretation:
        - **≥ 80** → Approved (personas are usable)
        - **< 80** → Rejected (must regenerate)

        -----------------------------------
        ### Output JSON Format (MANDATORY):

        {{
        "score": 0,
        "approved": false,
        "feedback": "Short explanation describing EXACTLY what is wrong or what is missing."
        }}
        -----------------------------------

        Return ONLY valid JSON.
        """

    
    response = query_groq(prompt, json_mode=True)
    return parse_json_output(response)
