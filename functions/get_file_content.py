import os
from config import MAX_CHARS
from google.genai import types

def get_file_content(working_directory, file_path):
    # Get working directory absolute path
    working_dir_abs = os.path.abspath(working_directory)
    # Create the target filepath
    target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
    # Create boolean flag for if the target file exists somewhere within the working directory
    target_in_working_dir = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs

    # Confirm that the target file exists within the working directory
    if not target_in_working_dir:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    # Confirm that the target is actually a file
    target_is_file = os.path.isfile(target_file)
    if not target_is_file:
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    try:
        # Read the target file
        with open(target_file, 'r') as f:
            # Read the maximum characters set in config.py
            content = f.read(MAX_CHARS)
            # Try to read one additional character - if f.read(1) returns "" (which is False-y) then the whole file was read. Anything other than "" returns True
            truncated = f.read(1)
            if truncated:
                content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'

            return content
    except Exception as e:
        return f'Error reading file {file_path}: {e}'
    
schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description=f"Retrieves the content (at most {MAX_CHARS} characters) of a specified file within the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to read, relative to the working directory",
            ),
        },
        required=["file_path"],
    ),
)