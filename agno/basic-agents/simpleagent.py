from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools

import os
from dotenv import load_dotenv
load_dotenv()

os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")

agent=Agent(
  model=Groq(id="qwen/qwen3-32b"),
  description="You are an assisstant please reply based on the questions",
  tools=[DuckDuckGoTools()],
  markdown=True
)

agent.print_response("Who won the india vs new zealand t20 world cup final match?")
