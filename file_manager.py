import os
from settings import WORKING_DIRECTORY

def create_folder(folder_name):
    folder_path = os.path.join(WORKING_DIRECTORY, folder_name)
    os.makedirs(folder_path, exist_ok=True)

def delete_folder(folder_name):
    folder_path = os.path.join(WORKING_DIRECTORY, folder_name)
    os.rmdir(folder_path)

def move_to(folder_name):
    global WORKING_DIRECTORY
    new_directory = os.path.join(WORKING_DIRECTORY, folder_name)
    if os.path.isdir(new_directory):
        WORKING_DIRECTORY = new_directory
    else:
        print("Folder not found.")

def move_up():
    global WORKING_DIRECTORY
    parent_directory = os.path.dirname(WORKING_DIRECTORY)
    if parent_directory != WORKING_DIRECTORY:
        WORKING_DIRECTORY = parent_directory
    else:
        print("Already at the top level.")

def create_file(file_name):
    file_path = os.path.join(WORKING_DIRECTORY, file_name)
    open(file_path, 'a').close()

def write_to_file(file_name, content):
    file_path = os.path.join(WORKING_DIRECTORY, file_name)
    with open(file_path, 'w') as file:
        file.write(content)

def view_file(file_name):
    file_path = os.path.join(WORKING_DIRECTORY, file_name)
    with open(file_path, 'r') as file:
        print(file.read())

def delete_file(file_name):
    file_path = os.path.join(WORKING_DIRECTORY, file_name)
    os.remove(file_path)

def copy_file(file_name, destination_folder):
    source_path = os.path.join(WORKING_DIRECTORY, file_name)
    destination_path = os.path.join(WORKING_DIRECTORY, destination_folder, file_name)
    if os.path.isfile(source_path):
        os.makedirs(os.path.join(WORKING_DIRECTORY, destination_folder), exist_ok=True)
        os.system(f'copy "{source_path}" "{destination_path}"')
    else:
        print("File not found.")

def move_file(file_name, destination_folder):
    source_path = os.path.join(WORKING_DIRECTORY, file_name)
    destination_path = os.path.join(WORKING_DIRECTORY, destination_folder, file_name)
    if os.path.isfile(source_path):
        os.makedirs(os.path.join(WORKING_DIRECTORY, destination_folder), exist_ok=True)
        os.rename(source_path, destination_path)
    else:
        print("File not found.")

def rename_file(old_name, new_name):
    old_path = os.path.join(WORKING_DIRECTORY, old_name)
    new_path = os.path.join(WORKING_DIRECTORY, new_name)
    if os.path.exists(old_path):
        os.rename(old_path, new_path)
    else:
        print("File not found.")

# Example usage:
if __name__ == "__main__":
    create_folder("test_folder")
    create_file("test.txt")
    write_to_file("test.txt", "Hello, World!")
    view_file("test.txt")
    move_to("test_folder")
    view_file("test.txt")
    move_up()
    delete_folder("test_folder")
