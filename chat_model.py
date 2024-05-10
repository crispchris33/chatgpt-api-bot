# chat_model.py
from config import chatgpt_model_version
from langchain_openai import ChatOpenAI

def get_chat_model():
    return ChatOpenAI(model=chatgpt_model_version, temperature=0.2)