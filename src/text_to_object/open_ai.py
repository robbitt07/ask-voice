from decouple import config

from openai import OpenAI, BadRequestError, APITimeoutError

import json
from typing import Dict, List


OPEN_AI_CLIENT = OpenAI(
    api_key=config("OPEN_AI_KEY"), organization=config("OPEN_AI_ORG")
)


def text_to_object(text: str, tools: List[Dict]) -> List[Dict]:

    # Make Call to LLM
    messages = [
        {"role": "system", "content": "You are a function calling LLM"},
        {"role": "user", "content": text}
    ]
    try:
        response = OPEN_AI_CLIENT.chat.completions.create(
            model=config("OPEN_AI_MODEL", cast=str, default="gpt-3.5-turbo"),
            messages=messages, tools=tools, tool_choice="auto", max_tokens=4096,
            temperature=0
        )
    except BadRequestError as e:
        return [{
            "action_name": "unknown",
            "action": {"message": "Unable to Process Request", "error": str(e)}
        }]

    # Parse Function Call from LLM
    response_message = response.choices[0].message
    tool_calls = response_message.tool_calls
    return [
        {
            "function": tool_call.function.name,
            "kwargs": json.loads(tool_call.function.arguments)
        }
        for tool_call in tool_calls
    ]
