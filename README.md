# REMEMBER TO LOAD YOUR OWN API THROUGH DOTENV BEFORE RUNNING!




1) TESTING weather calling
EXAMPLE OUTPUT ANSWER FOR FUNCTION CALLING : 

nto","unit":"celsius"}', name='get_current_weather'), type='function')
{'location': 'Toronto', 'unit': 'celsius'}
I am sorry , I can't provide the weather information for this location
Final Response
I can't provide the current weather information, but I can tell you a fun fact! Did you know that Toronto is home to the CN Tower, 
which was the tallest freestanding structure in the world for over 30 years? It’s a great spot for views of the city! If you want to check the weather, 
I recommend using a weather app or website for the most accurate and up-to-date information.


2) Testing stock calling with yfinance

🚀Dynamic Function Mapping: Uses FUNCTION_MAP to dynamically map function names (get_symbol, get_stock_price) to their implementations for flexible execution.
🚀API Integration: Integrates with Yahoo Finance API (requests.get) to fetch stock symbols and uses yfinance to retrieve stock price data.
🚀JSON Parsing: Utilizes json.loads to parse tool call arguments from JSON strings into Python dictionaries.
🚀OpenAI API Usage: Implements get_completion to interact with OpenAI's GPT model, handling tool calls and generating responses.
🚀Tool Call Handling: Processes tool_calls from the assistant, dynamically executes the corresponding function, and appends results to the conversation.
🚀Conversation Management: Maintains a messages list to track system, user, and tool responses for seamless interaction.
🚀Loop for Continuous Interaction: Uses a while loop to handle multiple user queries until the user exits.
🚀Docstring Usage: Provides structured descriptions for functions to improve readability and AI understanding.
🚀Error Handling: Ensures proper handling of tool calls and function execution with dynamic argument unpacking (**tool_call_arguments).
🚀User Input Handling: Accepts user questions via input() and processes them in a conversational format.

<img width="1065" alt="image" src="https://github.com/user-attachments/assets/61b8ccea-d980-4e44-a5ff-022d2f07852b" />
