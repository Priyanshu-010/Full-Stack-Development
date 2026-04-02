from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
load_dotenv()

from langchain_community.tools import DuckDuckGoSearchResults
from langchain_community.retrievers import ArxivRetriever
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

# duck duck go search results tool

# Allows you to search the web using duck duck go and get the results in a structured format. You can specify the number of results to retrieve and whether to get the full text of the results or just the snippets.

# duck_search = DuckDuckGoSearchResults()

# ans = duck_search.invoke("Latest news about LangGraph")

# print(ans)

# ARXIV RETRIEVER
# Allows you to query arxiv for papers and get the full text of the papers as well. You can specify the number of papers to retrieve and whether to get the full text or just the abstracts.


# arxiv_retriever = ArxivRetriever(
#     load_max_docs=2,
#     get_full_documents=True,
# )

# arxiv_ans = arxiv_retriever.invoke("transformers in NLP")
# print(arxiv_ans)

# WIKIPEDIA QUERY RUN

# Allows you to query Wikipedia and get the full text of the page as well. You can specify the number of results to retrieve and whether to get the full text or just the summary.

# wiki_query = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())
# wiki_ans = wiki_query.invoke("What is LangGraph?")
# print(wiki_ans)

# Tools

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


# Custom tool example

@tool
def personal_info(name: str):

  """Use this tool to get personal information about Alice, Bob, and Charlie."""
  info = {
    "Alice": "Alice is a software engineer with 5 years of experience in web development.",
    "Bob": "Bob is a data scientist with a background in machine learning and statistics.",
    "Charlie": "Charlie is a UX designer with a passion for creating intuitive and user-friendly interfaces."
  }

  return info.get(name, "No information available for this person.")

personal_info_ans = personal_info.invoke("Alice")
print(personal_info_ans)


# Binding the tools to the LLM

tools = [search_duckduckgo, arxiv_tool, wiki_tool, personal_info]

llm_with_tools = llm.bind_tools(tools)