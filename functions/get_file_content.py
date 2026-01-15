import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    working_dir_abs = os.path.abspath(working_directory)
    target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
    target_in_working_dir = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs

    if not target_in_working_dir:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    target_is_file = os.path.isfile(target_file)
    if not target_is_file:
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    try:
        with open(target_file, 'r') as f:
            content = f.read(MAX_CHARS)
            truncated = f.read(1)
            if truncated:
                content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'

            return content
    except Exception as e:
        return f'Error reading file {file_path}: {e}'