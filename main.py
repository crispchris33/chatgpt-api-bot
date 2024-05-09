# main.py
from chatbot import handle_chat

def start_chat():
    print("Chatbot is ready to talk! Type 'quit' to exit.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            break
        
        response = handle_chat(user_input)
        print("AI:", response)

if __name__ == "__main__":
    start_chat()
