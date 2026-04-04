from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
load_dotenv()

from typing import TypedDict, List
from langgraph.graph import StateGraph, START, END

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

class graph_schema(TypedDict):
    
    topic: str
    insta: str
    twitter: str
    linkedin: str


# functions for creating posts for different platforms

def create_post_insta(state: graph_schema) -> graph_schema:
    

    # Extract the topic from the state
    topic = state['topic']

    # Passing the topic to the LLM to generate an Instagram post
    post = llm.invoke(f"Write an Instagram post about {topic}. Keep the tone casual and engaging.").content

    # Update the state with the generated post
    state['insta'] = post

    return {'insta' : post}

def create_post_twitter(state: graph_schema) -> graph_schema:
    

    # Extract the topic from the state
    topic = state['topic']

    # Passing the topic to the LLM to generate a Twitter post
    post = llm.invoke(f"Write a Twitter post about {topic}. Keep the tone quick").content

    # Update the state with the generated post
    state['twitter'] = post

    return {'twitter' : post}


def create_post_linkedin(state: graph_schema) -> graph_schema:
    

    # Extract the topic from the state
    topic = state['topic']

    # Passing the topic to the LLM to generate a LinkedIn post
    post = llm.invoke(f"Write a LinkedIn post about {topic}. Keep the tone professional and informative.").content

    # Update the state with the generated post
    state['linkedin'] = post

    return {'linkedin' : post}

from langgraph.graph import StateGraph, START, END

graph = StateGraph(graph_schema)

graph.add_node("create_post_insta", create_post_insta)
graph.add_node("create_post_twitter", create_post_twitter)
graph.add_node("create_post_linkedin", create_post_linkedin)

# This is how we can create parallel edges from the START node to multiple nodes, allowing them to execute in parallel. Each of these nodes will take the same input (the topic) and generate posts for their respective platforms simultaneously. Finally, we can connect each of these nodes to the END node to signify the completion of the graph execution.

graph.add_edge(START, "create_post_insta")
graph.add_edge(START, "create_post_twitter")
graph.add_edge(START, "create_post_linkedin")
graph.add_edge("create_post_insta", END)
graph.add_edge("create_post_twitter", END)
graph.add_edge("create_post_linkedin", END)

parallel_graph = graph.compile()

# Image generation code (uncomment to generate the image)

# with open("graphs/graph4.png", "wb") as f:
#     f.write(parallel_graph.get_graph().draw_mermaid_png())


ans = parallel_graph.invoke({"topic": "Artificial Intelligence",
"insta": "","twitter": "","linkedin": ""})

print(ans)