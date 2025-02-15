import json
import os
import openai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve values
AIPROXY_TOKEN = os.getenv("AIPROXY_TOKEN")

openai.api_key = AIPROXY_TOKEN

def parse_task(task_description: str):
    prompt = f"Extract structured information from the following task: {task_description}. Output in JSON format."

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": prompt}],
        temperature=0.2
    )

    try:
        return json.loads(response["choices"][0]["message"]["content"])
    except json.JSONDecodeError:
        raise ValueError("Failed to parse LLM response")
