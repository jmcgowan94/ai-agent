import os

def get_files_info(working_directory, directory="."):
    working_dir_abs = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
    valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs

    if not valid_target_dir:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory\n'
    
    target_is_dir = os.path.isdir(target_dir)
    if not target_is_dir:
        return f'{directory} is not a directory\n'
    
    # print(f'Accessing {target_dir}...')
    dir_items = os.listdir(target_dir)
    return_str = ""
    for item in dir_items:
        try:
            file_size = os.path.getsize(f'{target_dir}/{item}')
        except Exception as e:
            print(f'Error getting file size for {item}: {e}\n')
        try:
            is_dir = os.path.isdir(f'{target_dir}/{item}')
        except Exception as e:
            print(f'Error determining item type for {item}: {e}\n')
        item_str = f'- {item}: file_size={file_size} bytes, is_dir={is_dir}'
        return_str += item_str+"\n"
    return return_str
