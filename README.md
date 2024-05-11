# chatgpt-api-bot

This chatbot project is designed to interact with users, read files from a specified directory, and utilize OpenAI's models to process various inputs. It supports reading plain text, JSON, CSV, programming files, and image files, among others.

## Dependencies

- langchain
- langchain-openai
- python-dotenv
- openai

## Getting Started

Follow these steps to set up and run the chatbot project on your local machine.

### Prerequisites

Ensure you have Python installed on your machine. This project requires Python 3.7 or higher.

### Installation

1. Clone the Repository
   Alternatively, you can download the ZIP file of the project and extract it.

2. Set Up a Virtual Environment

   On macOS and Linux:
   python3 -m venv env
   source env/bin/activate

   On Windows:
   python -m venv env
   .\env\Scripts\activate

3. Install Dependencies

   Install the required Python packages by running:
   pip install -r requirements.txt

### Configuration

1. Environment Variables

   Create a .env file in the root directory of your project and add your OpenAI API key and the local file path from which the bot should read files:
   OPENAI_API_KEY=your_openai_api_key_here
   LOCAL_FILE_PATH=your_file_directory_path_here
   CHARACTER_LIMIT=4000
   CHATGPT_MODEL_VERSION=gpt-3.5-turbo

   Replace your_openai_api_key_here with your actual OpenAI API key and your_file_directory_path_here with the full path to the directory containing the files you want the bot to read.

   Note: There is also an example .env file provided. Change the name to ".env" when ready to use.

### Usage

To run the chatbot, execute the following command in the root directory of your project:

python main.py

### Interacting with the Chatbot

Once the chatbot is running, you can interact with it by typing messages. Here are some examples of what you can do:

#### General Conversation

Just type your message and get a response. For example:

You: Hello, how are you?

#### Read Files

To read one or more files, use the command read files followed by the file names. For example:

You: read files example.txt options.html

This will display the content of example.txt and options.html.

### Supported File Types

The chatbot can read and process the following types of files:

- Plain text files (.txt)
- Programming files (.py, .js, .html, .css, .java, .cpp, .c, .sh, .md)
- JSON files (.json)
- CSV files (.csv)
- Image files (.jpg, .jpeg, .png, .gif, .bmp) - displayed as base64 strings
