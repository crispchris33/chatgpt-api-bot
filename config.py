# config.py
import os
import dotenv

dotenv.load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
local_file_path = os.getenv("LOCAL_FILE_PATH")
