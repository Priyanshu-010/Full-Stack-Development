from tools import get_stock_price
from memory import save_chat, get_history

def run_agent(user_id: str, message:str):
  history = get_history(user_id)

  if "price" in message.lower():
      words = message.split()
      symbol = words[-1]
      result = get_stock_price(symbol)
      response = f"The price of {symbol} is {result}"
  else:
      response = "I can help you with stock prices."
  save_chat(user_id, message, response)

  return response