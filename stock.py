import os 
import requests
from dotenv import load_dotenv
import yfinance as yf
import pandas as pd 

#hmm
import inspect
from pydantic import TypeAdapter
from pydantic import Basemodel
from openai import OpenAI
load_dotenv()



def get_symbol(company: str) -> str:
    url = "https://query2.finance.yahoo.com/v1/finance/search"
    params = {"q": company, "country" : "United States"}
    user_agents = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    response = requests.get(url,params=params,headers=user_agents)
    data = response.json()
    return data["quotes"][0]["symbol"]


print(get_symbol("Apple Inc."))

def get_stock_price(symbol: str):
    stock = yf.Ticker(symbol)
    hist = stock.history(period="1d", interval="1m")
    latest = hist.iloc[-1]
    return {
        "timestamp": str(latest.name),
        "open": latest["Open"],
        "high": latest["High"],
        "low": latest["Low"],
        "close": latest["Close"],
        "volume": latest["Volume"]
    }

print(get_stock_price("AAPL"))

tool = [
    {
        "type":"function",
        "function":{
        "name":"get_symbol",
        "description": inspect.getdoc(get_symbol),
        "parameters": TypeAdapter(get_symbol).json_schema()
    }
    }
]

print(tool)


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY)"))

message = [
    {
        "role":"system",
        "content": "you are a helpful assistant thatcan retreive stock prices for a given company"
    }
]
                
                
