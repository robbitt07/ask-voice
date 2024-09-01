from text_to_object.groq import text_to_object as text_to_object_groq
from text_to_object.open_ai import text_to_object as text_to_object_open_ai

from decouple import config
from logging import getLogger
from typing import Dict, List

logger = getLogger("service")


def text_to_object(text: str, tools: List[Dict]) -> Dict:
    if config("GROQ_API_KEY"):
        return text_to_object_groq(text=text, tools=tools)

    elif config("OPEN_AI_KEY"):
        return text_to_object_open_ai(text=text, tools=tools)

    raise None
