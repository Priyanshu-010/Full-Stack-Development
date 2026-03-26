from agno.agent import Agent
from agno.team import Team
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools

import os
from dotenv import load_dotenv
load_dotenv()

os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")


web_agent=Agent(
  name="Web Agent",
  role="Search the web for information",
  model=Groq(id="qwen/qwen3-32b"),
  tools=[DuckDuckGoTools()],
  instructions="Always include the sources",
  markdown=True
) 
finance_agent=Agent(
  name="Finance Agent",
  role="Get Financial data",
  model=Groq(id="qwen/qwen3-32b"),
  tools=[YFinanceTools()],
  instructions="Use Tables to display data",
  markdown=True
)

agent_team=Team(
  members=[web_agent, finance_agent],
  model=Groq(id="qwen/qwen3-32b"),
  instructions=["Always include the sources", "Use Tables to display data"],
  markdown=True
)

agent_team.print_response("Analyze companies like tesla, Nvidia, apple and suggest which to but for long term")
