from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
load_dotenv()

from typing import TypedDict, List
from langgraph.graph import StateGraph, START, END
from IPython.display import Image, display

if os.environ['GROQ_API_KEY']:
  print("GROQ API KEY FOUND")
else:
  raise ValueError("GROQ API KEY NOT FOUND")

llm = ChatGroq(
    model="qwen/qwen3-32b",
    temperature=0,
    max_tokens=None,
    reasoning_format="parsed",
    timeout=None,
    max_retries=2,
)

# messages = [
#     (
#         "system",
#         "You are a helpful assistant that answer the user questions",
#     ),
#     ("human", "what is water"),
# ]
# ai_msg = llm.invoke(messages)
# print(ai_msg.content)

class graph_schema(TypedDict):
  name: str
  message: str


def welcome(state: graph_schema)->graph_schema:
  curr_name = state['name']
  curr_message = state['message']

  response = llm.invoke(f"My name is {curr_name}. {curr_message}").content

  state["message"] = f" Your message was '{curr_message}'. Here's my response:  {response}"
  return state


graph = StateGraph(graph_schema)

# Adding Nodes
graph.add_node("welcome", welcome)

# Adding Edges 
graph.add_edge(START, "welcome")
graph.add_edge("welcome", END)

first_graph = graph.compile()

# to generate a graph image in jupyter notebook you can use the below code

# Image(first_graph.get_graph().draw_mermaid_png())

# Use this code to save the graph image in a file as I have done the above code is for jupyter notebook

# with open("graph.png", "wb") as f:
#     f.write(first_graph.get_graph().draw_mermaid_png())

#when the code gives any error, you can use the below code to print the mermaid graph and debug it.

# print(first_graph.get_graph().draw_mermaid())

ans = first_graph.invoke({"name": "Priyanshu", "message": "How are you?"})
print(ans)