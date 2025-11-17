import os
import json
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage

load_dotenv()

def call_groq_json(system_prompt, user_prompt, model="llama-3.3-70b-versatile"):

    key = os.getenv("GROQ_API_KEY")
    if not key:
        raise RuntimeError("❌ Missing GROQ_API_KEY")

    llm = ChatGroq(
        api_key=key,
        model=model,
        temperature=0.2,
        response_format={"type": "json_object"}   # << 🚨 THIS FORCES JSON
    )

    result = llm.invoke([
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_prompt),
    ])

    try:
        return json.loads(result.content)
    except Exception:
        print("\n⚠ MODEL RAW OUTPUT:\n", result.content, "\n")
        raise ValueError("❌ Model output was NOT valid JSON")
