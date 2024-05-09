# chatgpt-api-bot

Dependencies:

langchain
langchain-openai
python-dotenv
openai

# Chatbot Project

This chatbot project is designed to interact with users, read files from a specified directory, and utilize OpenAI's models for processing various inputs. It supports reading plain text, JSON, CSV, and programming files, among others.

## Getting Started

Follow these steps to set up and run the chatbot project on your local machine.

### Prerequisites

Ensure you have Python installed on your machine. This project requires Python 3.7 or higher.

# Installation

Clone the Repository

Otherwise, you can download the ZIP file of the project and extract it.
Set Up a Virtual Environment by running:

On macOS and Linux:

python3 -m venv env
source env/bin/activate

On Windows:

python -m venv env
.\env\Scripts\activate

# Install Dependencies

Install the required Python packages by running:

pip install -r requirements.txt

# Configuration

Environment Variables

Create a .env file in the root directory of your project and add your OpenAI API key and the local file path from which the bot should read files:

OPENAI_API_KEY=your_openai_api_key_here
LOCAL_FILE_PATH=your_file_directory_path_here

**There is also an example env file provided but change the name to ".env" when ready to use.

Replace your_openai_api_key_here with your actual OpenAI API key and your_file_directory_path_here with the full path to the directory containing the files you want the bot to read.

# Usage

To run the chatbot, execute the following command in the root directory of your project:

python main.py

# Interacting with the Chatbot

Once the chatbot is running, you can interact with it by typing messages. Here are some things you can do:

General Conversation:

Just type your message and get a response. For example:

You: Hello, how are you?

Read Files:

To read a file, use the command read file followed by the file name. For example:

You: read file example.txt

This will display the content of example.txt.

# Supported File Types

The chatbot can read the following types of files:

Plain text files (.txt)
Programming files (.py, .js, .html, .css, .java, .cpp, .c, .sh, .md)
JSON files (.json)
CSV files (.csv)
Image files (.jpg, .jpeg, .png, .gif, .bmp) as base64 strings