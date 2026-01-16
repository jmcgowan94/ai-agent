import os
import subprocess

def run_python_file(working_directory, file_path, args=None):
    # Get working directory absolute path
    working_dir_abs = os.path.abspath(working_directory)
    # Create the target filepath
    target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
    # Create boolean flag for if the target file exists somewhere within the working directory
    target_in_working_dir = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs

    # Confirm that the target file exists within the working directory
    if not target_in_working_dir:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    # Confirm that target is a file
    target_is_file = os.path.isfile(target_file)
    if not target_is_file:
        return f'Error: "{file_path}" does not exist or is not a regular file'
    
    # Confirm that target is a .py file
    if not target_file.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file'
    
    # Create subprocess
    absolute_file_path = target_file
    command = ["python", absolute_file_path]
    if args is not None:
        command.extend(args)

    try:
        completed = subprocess.run(command, cwd=working_dir_abs, capture_output=True, text=True, timeout=30)
        output = []
        if completed.returncode != 0:
            output.append(f'Process exited with code {completed.returncode}')
        if not completed.stdout and not completed.stderr:
            output.append('No output produced')
        if completed.stdout:
            output.append(f'STDOUT: {completed.stdout}')
        if completed.stderr:
            output.append(f'STDERR: {completed.stderr}')
        
        return "\n".join(output)
    except Exception as e:
        return f'Error executing Python file: {e}'
    