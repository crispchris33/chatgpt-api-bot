#file_reader.py
import os
import json
import csv
import base64
from config import character_limit, local_file_path

def read_local_files(file_names):
    files_content = {}
    for file_name in file_names:
        full_path = os.path.join(local_file_path, file_name)
        extension = os.path.splitext(file_name)[1].lower()
        
        try:
            if extension in ['.txt', '.py', '.js', '.html', '.css', '.java', '.cpp', '.c', '.sh', '.md', '.json']:
                with open(full_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    files_content[file_name] = content

            elif extension == '.csv':
                with open(full_path, mode='r', encoding='utf-8') as file:
                    csv_reader = csv.DictReader(file)
                    content = list(csv_reader)
                    content_str = json.dumps(content)
                    files_content[file_name] = content_str

            elif extension in ['.jpg', '.jpeg', '.png', '.gif', '.bmp']:
                with open(full_path, 'rb') as file:
                    content = base64.b64encode(file.read()).decode('utf-8')
                    files_content[file_name] = content

            else:
                files_content[file_name] = f"Unsupported file extension: {extension}"
        
        except FileNotFoundError:
            files_content[file_name] = f"File not found: {full_path}"
        except Exception as e:
            files_content[file_name] = f"Error reading file: {str(e)}"
    
    return files_content