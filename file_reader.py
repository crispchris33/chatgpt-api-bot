# file_reader.py
import os
import json
import csv
import base64
from config import character_limit, local_file_path

def read_local_file(file_name):
    full_path = os.path.join(local_file_path, file_name)
    extension = os.path.splitext(file_name)[1].lower()
    
    try:
        if extension in ['.txt', '.py', '.js', '.html', '.css', '.java', '.cpp', '.c', '.sh', '.md', '.json']:
            with open(full_path, 'r', encoding='utf-8') as file:
                content = file.read()
                return content[:character_limit]  # Use character limit from config

        elif extension == '.csv':
            with open(full_path, mode='r', encoding='utf-8') as file:
                csv_reader = csv.DictReader(file)
                return list(csv_reader) 
        
        elif extension in ['.jpg', '.jpeg', '.png', '.gif', '.bmp']:
            with open(full_path, 'rb') as file:
                return base64.b64encode(file.read()).decode('utf-8')
        
        else:
            return f"Unsupported file extension: {extension}"
    
    except FileNotFoundError:
        return f"File not found: {full_path}"
    except Exception as e:
        return f"Error reading file: {str(e)}"
