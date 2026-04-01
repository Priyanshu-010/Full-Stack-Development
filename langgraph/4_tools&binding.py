from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
load_dotenv()

from langchain_community.tools import DuckDuckGoSearchResults
from langchain_community.retrievers import ArxivRetriever


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

# duck_search = DuckDuckGoSearchResults()

# ans = duck_search.invoke("Latest news about LangGraph")

# print(ans)


arxiv_retriever = ArxivRetriever(
    load_max_docs=2,
    get_full_documents=True,
)

arxiv_ans = arxiv_retriever.invoke("transformers in NLP")
print(arxiv_ans)