import argparse
import json
import os

from openai import OpenAI

API_KEY = os.getenv("OPENROUTER_API_KEY")
BASE_URL = os.getenv("OPENROUTER_BASE_URL", default="https://openrouter.ai/api/v1")

TOOLS = [{
    "type": "function",
    "function": {
        "name": "Read",
        "description": "Read and return the contents of a file",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "The path to the file to read"
                }
            },
            "required": ["file_path"]
        }
    }
}]


def execute_tool(name, args):
    if name == "Read":
        with open(args["file_path"], "r") as f:
            return f.read()
    raise ValueError(f"Unknown tool: {name}")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("-p", required=True)
    args = p.parse_args()

    if not API_KEY:
        raise RuntimeError("OPENROUTER_API_KEY is not set")

    client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

    messages = [{"role": "user", "content": args.p}]

    while True:
        chat = client.chat.completions.create(
            model="anthropic/claude-haiku-4.5",
            messages=messages,
            tools=TOOLS,
        )

        if not chat.choices:
            raise RuntimeError("no choices in response")

        choice = chat.choices[0]
        message = choice.message
        messages.append(message)

        if not message.tool_calls or choice.finish_reason == "stop":
            print(message.content)
            break

        for tool_call in message.tool_calls:
            tool_args = json.loads(tool_call.function.arguments)
            result = execute_tool(tool_call.function.name, tool_args)
            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": result,
            })


if __name__ == "__main__":
    main()