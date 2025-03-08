from openai import OpenAI
import os
from dotenv import load_dotenv
import json

def get_current_weather(location: str, unit: str):
    if location == "Barrie , Ontario , Canada" and unit == "celsius":
        return "It is so cold right now , you should wear a jacket"
    elif location == "Toronto , Ontario , Canada" and unit == "fahrenheit":
        return "Toronto is bad , you should wear a jacket"
    else:
        return "I am sorry , I can't provide the weather information for this location"

def get_stock_price(symbol: str):

    pass


def view_website(url: str):

    pass


tools = [
    {
        "type": "function",
        "function": {
            "name": "get_current_weather",
            "description": "Get the current weather in a given location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city name"
                    },
                    "unit": {
                        "type": "string",
                        "enum": ["celsius", "fahrenheit"],
                        "description": "The temperature unit"
                    }
                },
                "required": ["location", "unit"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_stock_price",
            "description": "Get the current stock price of a given symbol",
            "parameters": {"type": "object", "properties": {"symbol": {"type": "string"}}, "required": ["symbol"]}
        }
    },
    {
        "type": "function",
        "function": {
            "name": "view_website",
            "description": "View a website",
            "parameters": {"type": "object", "properties": {"url": {"type": "string"}}, "required": ["url"]}
        }
    }
]


load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

messages = [
    {"role":"system","content" : "You are helpful assistant,answer something fun"},
    {"role":"user","content":"What is the weather today! in Toronto , Ontario , Canada"}
]

response = client.chat.completions.create(
    model="gpt-4o-mini",
    tools=tools,
    messages=messages
)


#for sorting the response except of the json.
tool_call = response.choices[0].message.tool_calls[0]
arguments = json.loads(tool_call.function.arguments)

print(tool_call)
print(arguments)

if tool_call.function.name == "get_current_weather":
    current_weather = get_current_weather(
        arguments.get("location"), arguments.get("unit"))
    print(current_weather)
    
    #append msg cu
    messages.append(response.choices[0].message)
    #append msg from tool
    messages.append({"role":"tool","tool_call_id": tool_call.id, "content": current_weather})

    final_response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages   
    )
    print("Final Response")
    print(final_response.choices[0].message.content)
