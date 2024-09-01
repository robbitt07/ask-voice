from decouple import config
from groq import Groq, BadRequestError

from datetime import datetime
from functools import lru_cache
import json
from typing import Dict, List


@lru_cache
def get_groq_llm():
    return Groq(api_key=config("GROQ_API_KEY"))


def text_to_object(text: str, tools: List[Dict]) -> Dict:

    # Make Call to LLM
    start = datetime.now()
    llm = get_groq_llm()
    messages = [
        {"role": "system", "content": "You are a function calling LLM"},
        {"role": "user", "content": text}
    ]
    try:
            
        response = llm.chat.completions.create(
            model=config("GROQ_MODEL"), messages=messages, tools=tools,
            tool_choice="auto", max_tokens=4096, temperature=0
        )
    except BadRequestError as e:
        return [{
            "action_name": "unknown",
            "action": {"message": "Unable to Process Request", "error": str(e)}
        }]

    end = datetime.now()
    print(f"Response time: {(end - start).total_seconds():,.2f}")

    # Parse Function Call from LLM
    response_message = response.choices[0].message
    tool_calls = response_message.tool_calls
    return [
        {
            "action_name": tool_call.function.name,
            "action": json.loads(tool_call.function.arguments)
        }
        for tool_call in tool_calls
    ]
