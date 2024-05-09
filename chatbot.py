# chatbot.py
from langchain_core.messages import HumanMessage, AIMessage
from langchain.memory import ChatMessageHistory
from config import local_file_path
from file_reader import read_local_file  # Import from file_reader.py
from chat_model import get_chat_model

chat_model = get_chat_model()
chat_history = ChatMessageHistory()

def handle_chat(user_input):
    chat_history.add_user_message(HumanMessage(content=user_input))
    
    if user_input.lower().startswith("read file "):
        file_name = user_input[len("read file "):].strip()
        file_content = read_local_file(file_name, local_file_path)
        
        if isinstance(file_content, (dict, list)):
            file_content_str = json.dumps(file_content, indent=2)
        else:
            file_content_str = str(file_content)
        
        chat_history.add_ai_message(AIMessage(content=file_content_str))
        return file_content_str
    
    try:
        messages = chat_history.messages
        response = chat_model.invoke(messages)
        response_text = response.content if isinstance(response, AIMessage) else str(response)
        chat_history.add_ai_message(AIMessage(content=response_text))
        return response_text

    except Exception as e:
        print(f"An error occurred: {e}")
        return "Error processing your message. Please try again."
