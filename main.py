from openai import OpenAI
import os
from dotenv import load_dotenv


def get_current_weather(location: str, unit: str):

    return "It is so cold right now , you should wear a jacket"

def get_stock_price(symbol: str):

    pass


def view_website(url: str):

    pass


tools = [
    {
        "type": "function",
        "function":{
            "name": "get_current_weather",
            "description": "Get the current weather of a location",
            "parameters": [
                {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "The city name"
                        },
                        "unit": {
                            "type": "string",
                            "enum": ["C", "F"],
                            "description": "The unit of the weather"
                        }
                    }
                }
            ]

        }
    },
    {
        "type": "function",
        "function":{
            "name": "get_stock_price",
            "description": "Get the stock price of a company",
            "parameters": {
                "type": "object",
                "properties": {
                    "symbol": {
                        "type": "string",
                        "required": "The stock symbol"
                    }
                }
            }
        }
    },
    {
        "type": "function",
        "function":{
            "name": "view_website",
            "description": "View a website",
            "parameters": {
                "type": "object",
                "properties": {
                    "url": {
                        "type": "string",
                        "description": "The website url"
                    }
                }
            }
        }
    }
]

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

message = [
    {"role":"system","content" : "You are helpful assistant"},
    {"role":"user","content":"What is the weather today!"}
]

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=message,
    tools = tools
)


print(response)