import os
from groq import Groq
from dotenv import load_dotenv
import json

load_dotenv()

def get_groq_client():
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        # For development/testing, you might want to handle this gracefully
        # or rely on the user providing it in the UI if not in env
        return None
    return Groq(api_key=api_key)

def query_groq(prompt, model="openai/gpt-oss-20b", json_mode=False):
    client = get_groq_client()
    if not client:
        raise ValueError("GROQ_API_KEY not found in environment variables.")

    messages = [
        {"role": "user", "content": prompt}
    ]
    
    kwargs = {
        "messages": messages,
        "model": model,
    }
    
    if json_mode:
        kwargs["response_format"] = {"type": "json_object"}

    chat_completion = client.chat.completions.create(**kwargs)
    
    return chat_completion.choices[0].message.content

def parse_json_output(output_str):
    try:
        return json.loads(output_str)
    except json.JSONDecodeError:
        # Attempt to find JSON block if wrapped in markdown
        import re
        match = re.search(r'```json\n(.*?)\n```', output_str, re.DOTALL)
        if match:
            try:
                return json.loads(match.group(1))
            except json.JSONDecodeError:
                pass
        return None
