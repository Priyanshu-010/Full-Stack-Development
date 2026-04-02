from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
load_dotenv()

from typing import TypedDict, List

from langchain_core.prompts import ChatPromptTemplate

from langchain_community.tools import DuckDuckGoSearchResults
from langchain_community.tools import ArxivQueryRun
from langchain_community.utilities import ArxivAPIWrapper
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import tool

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
    messages: List

@tool
def search_duckduckgo(query: str) -> str:

    """This tool searches the latest news on DuckDuckGo for the given query and returns the results."""
    duck_search = DuckDuckGoSearchResults()
    return duck_search.invoke(query)

@tool
def arxiv_tool(query: str) -> str:

    """"This tool allows you to query the arXiv database for research papers."""
    arxiv_query = ArxivQueryRun(api_wrapper=ArxivAPIWrapper())
    return arxiv_query.invoke(query)


@tool
def wiki_tool(query: str):

    """This tool allows you to search Wikipedia for information on a given topic."""
    wiki_query = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())
    return wiki_query.invoke(query)


@tool
def personal_info(name: str):

    """Use this tool to get personal information about Alice, Bob, or Charlie. 
    """

    info = {
        "Alice": "Alice is a software engineer with 5 years of experience in AI.",
        "Bob": "Bob is a data scientist who loves working with large datasets.",
        "Charlie": "Charlie is a product manager with a background in tech startups."
    }
    return info.get(name, "No information available for this person.")

tools = [search_duckduckgo, arxiv_tool, wiki_tool, personal_info]

llm_with_tools = llm.bind_tools(tools)

# LangGraph Creation

def llm_node(state:graph_schema) -> graph_schema:
   messages = state['messages']
   # Prompt template for the LLM
   prompt = ChatPromptTemplate.from_messages(
      [
        ("system", "You are a helpful assistant that can use tools to answer questions and provide information."),
        ("human", "{input}")
      ]
   )

   # LLM with tools
   chain = prompt | llm_with_tools
   response = chain.invoke({input: messages})

   state['messages'] = messages + [response]

   return state