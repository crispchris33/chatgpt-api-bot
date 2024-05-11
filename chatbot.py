# chatbot.py
from langchain_core.messages import HumanMessage, AIMessage
from langchain.memory import ChatMessageHistory
from file_reader import read_local_files
from chat_model import get_chat_model

chat_model = get_chat_model()
chat_history = ChatMessageHistory()

def handle_chat(user_input):
    chat_history.add_user_message(HumanMessage(content=user_input))
    
    if user_input.lower().startswith("read files"):
        file_names = user_input.split()[2:]
        files_content = read_local_files(file_names)
        
        response = []
        for file_name, content in files_content.items():
            response.append(f"Content of {file_name}:\n{content}\n")
        response_text = "\n".join(response)
        chat_history.add_ai_message(AIMessage(content=response_text))
        return response_text
    
    try:
        messages = chat_history.messages
        response = chat_model.invoke(messages)
        response_text = response.content if isinstance(response, AIMessage) else str(response)
        chat_history.add_ai_message(AIMessage(content=response_text))
        return response_text

    except Exception as e:
        print(f"An error occurred: {e}")
        return "Error processing your message. Please try again."