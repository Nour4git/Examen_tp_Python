
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    model="llama3-70b-8192",
    temperature=0.7,
    max_tokens=500,
    api_key=os.environ["GROQ_API_KEY"]
)
def generate_summary_with_llm(prompt: str) -> str:
    return llm.invoke(prompt).content
