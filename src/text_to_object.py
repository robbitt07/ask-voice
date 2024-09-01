from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.schema import HumanMessage, SystemMessage

from functions import tools

from decouple import config
from datetime import datetime
import json
from typing import Dict, List


def pprint(val):
    print(json.dumps(val, indent=2))


llm = ChatOpenAI(
    model="gpt-3.5-turbo", api_key=config("OPEN_AI_KEY"),
    organization=config("OPEN_AI_ORG"), temperature=0, streaming=True
)


def prompt_to_object(prompt: str) -> List[Dict]:

    system_msg = SystemMessage(
        content="You are a commodity trader assistant the helps with entering contracts and saving followup tasks."
    )

    template = PromptTemplate(
        input_variables=['content'],
        output_parser=None,
        partial_variables={},
        template="""{content}\n
        Ensure that all required field are meet. Be precise and ask the user to clarify if unclear\n\n
        """,
        template_format='f-string',
        validate_template=True
    )

    # Make Call to LLM
    start = datetime.now()
    llm_response = llm.invoke(
        input=[
            system_msg, HumanMessage(content=template.format(content=prompt))
        ], tools=tools
    )
    if "tool_calls" not in llm_response.additional_kwargs:
        return []

    tool_calls = llm_response.additional_kwargs["tool_calls"]
    end = datetime.now()
    print(f"Response time: {(end - start).total_seconds():,.2f}")

    # Parse Function Call from LLM
    tool_calls = llm_response.additional_kwargs["tool_calls"]
    return [
        {
            "action_name": tool_call["function"]["name"],
            "action": json.loads(tool_call["function"]["arguments"])
        }
        for tool_call in tool_calls
    ]
