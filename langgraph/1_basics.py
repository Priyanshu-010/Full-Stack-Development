from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
load_dotenv()


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

messages = [
    (
        "system",
        "You are a helpful assistant that answer the user questions",
    ),
    ("human", "what is water"),
]
ai_msg = llm.invoke(messages)
print(ai_msg.content)