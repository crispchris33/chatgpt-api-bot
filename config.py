# config.py
import os
import dotenv

dotenv.load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
local_file_path = os.getenv("LOCAL_FILE_PATH")

#Character Limit (User Value,Default Value)
character_limit = int(os.getenv("CHARACTER_LIMIT", "2000"))

#GPT Version (User value, Default)
chatgpt_model_version = os.getenv("CHATGPT_MODEL_VERSION", "gpt-3.5-turbo")