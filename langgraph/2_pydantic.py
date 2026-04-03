from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
load_dotenv()
from pydantic import BaseModel, Field
from langgraph.graph import StateGraph, START, END
# from IPython.display import Image, display

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

class graph_schema(BaseModel):
  topic: str = Field(description="The topic of the conversation")
  post: str = Field(description="The LinkedIn post content")
  curated_post: str = Field(description="The curated LinkedIn post content")

demo_obj = graph_schema(
  topic="AI in Healthcare",
  post="AI is transforming healthcare by improving diagnostics and patient care.",
  curated_post="Here's a curated version of the post..."
)

def create_post(state: graph_schema)-> graph_schema:
  topic = state.topic

  post = llm.invoke(f"Create a LinkedIn post about {topic}").content

  state.post = post
  return state

def curate_post(state: graph_schema)-> graph_schema:
  post = state.post

  curated_post = llm.invoke(f"Curate the following LinkedIn post for better engagement: {post}").content

  state.curated_post = curated_post
  return state

graph = StateGraph(graph_schema)

graph.add_node("create_post", create_post)
graph.add_node("curate_post", curate_post)

graph.add_edge(START, "create_post")
graph.add_edge("create_post", "curate_post")
graph.add_edge("curate_post", END)

pydantic_graph = graph.compile()

with open("graphs/graph2.png", "wb") as f:
    f.write(pydantic_graph.get_graph().draw_mermaid_png())

ans = pydantic_graph.invoke({
  "topic": "AI in Healthcare",
  "post": "",
  "curated_post": ""
})

print(ans)