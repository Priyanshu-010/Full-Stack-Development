from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
load_dotenv()

from langchain_core.prompts import ChatPromptTemplate

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

my_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that answers questions about the world."),
    ("human", "I want to create a post about {topic}."),
])

prompt_filled = my_prompt.invoke({"topic": "the benefits of exercise"})
ans = llm.invoke(prompt_filled)

print(ans)

# Chain with prompts

# chain = my_prompt | llm
# chain_ans = chain.invoke({"topic": "the benefits of exercise"})

# print(chain_ans)