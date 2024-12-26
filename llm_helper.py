from dotenv import load_dotenv
from langchain_groq import ChatGroq
import os

load_dotenv()

groq_key = os.getenv("GROQ_KEY")
if not groq_key:
    raise ValueError("GROQ_KEY is not set. Please ensure it is defined in the .env file.")

llm = ChatGroq(api_key=groq_key, model_name="llama-3.2-90b-vision-preview")

if __name__ == "__main__":
    reply = llm.invoke("What are the main ingredients in samosa?")
    print(reply.content)
