import os
from google.genai import types


def write_file(working_directory, file_path, content):
    # Get working directory absolute path
    working_dir_abs = os.path.abspath(working_directory)
    # Create the target filepath
    target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
    # Create boolean flag for if the target file exists somewhere within the working directory
    target_in_working_dir = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs

    # Confirm that the target file exists within the working directory
    if not target_in_working_dir:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    # Confirm that the target is not a directory
    target_is_dir = os.path.isdir(target_file)
    if target_is_dir:
        return f'Error: Cannot write to "{file_path}" as it is a directory'
    
    # Confirm that all parent directories of the target file exist
    try:
        parent_dirs = os.path.dirname(target_file)
        os.makedirs(parent_dirs, exist_ok=True)
    except Exception as e:
        return f'Error creating parent directories: {e}'

    # Open the file in write mode
    try:
        with open(target_file, 'w') as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error writing to {file_path}: {e}'
    
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes text content to a specified file within the working directory (overwriting if the file exists)",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to write, relative to the working directory",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Text content to write to the file",
            ),
        },
        required=["file_path", "content"],
    ),
)