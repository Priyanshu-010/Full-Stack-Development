import os
from dotenv import load_dotenv
from google import genai

from tools import get_stock_price
from memory import save_chat, get_history

# Load env variables
load_dotenv()

# Create a Gemini client
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def run_agent(user_id: str, message: str):
    # Step 1: get memory
    history = get_history(user_id)

    # Step 2: format history
    history_text = ""
    for msg, res in history:
        history_text += f"User: {msg}\nAI: {res}\n"

    # Step 3: system prompt
    system_prompt = """
You are a financial assistant.

RULES:
- If user asks for stock/crypto price, respond EXACTLY like:
  CALL_TOOL: get_stock_price SYMBOL

- Otherwise, respond normally.
"""

    full_prompt = system_prompt + "\n\n" + history_text + "\nUser: " + message

    # Step 4: call Gemini
    response = client.models.generate_content(
        model="gemini-2.5-flash", # Use a current model name
        contents=full_prompt
    )
    output = response.text.strip()

    # Step 5: check for tool call
    if "CALL_TOOL" in output:
        parts = output.split()
        symbol = parts[-1]
        tool_result = get_stock_price(symbol)
        final_response = f"The price of {symbol} is {tool_result}"
    else:
        final_response = output

    # Step 6: save memory
    save_chat(user_id, message, final_response)

    return final_response   