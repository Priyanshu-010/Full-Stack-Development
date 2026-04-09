from typing import Annotated
from typing_extensions import TypedDict

from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()

from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages

class State(TypedDict):
  messages: Annotated[list, add_messages]


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
  

def chatbot(state: State):
  return {"messages": [llm.invoke(state["messages"])]}

graph_builder = StateGraph(State)

# Adding Nodes
graph_builder.add_node("llmchatbot", chatbot)

# Adding Edges
graph_builder.add_edge(START, "llmchatbot")
graph_builder.add_edge("llmchatbot", END)

#Compile the graph
graph = graph_builder.compile()
ans = graph.invoke({"messages": "Hi"})
print(ans["messages"][-1].content)