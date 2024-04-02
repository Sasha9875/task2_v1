import os
from settings import WORKING_DIRECTORY
import sys


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

def print_menu():
    print("File Manager Menu:")
    print("1. Create Folder")
    print("2. Delete Folder")
    print("3. Move to Folder")
    print("4. Move Up")
    print("5. Create File")
    print("6. Write to File")
    print("7. View File")
    print("8. Delete File")
    print("9. Copy File")
    print("10. Move File")
    print("11. Rename File")
    print("0. Exit")

def main():
    while True:
        print_menu()
        choice = input("Enter your choice: ")
        
        if choice == "1":
            folder_name = input("Enter folder name: ")
            create_folder(folder_name)
        elif choice == "2":
            folder_name = input("Enter folder name: ")
            delete_folder(folder_name)
        elif choice == "3":
            folder_name = input("Enter folder name: ")
            move_to(folder_name)
        elif choice == "4":
            move_up()
        elif choice == "5":
            file_name = input("Enter file name: ")
            create_file(file_name)
        elif choice == "6":
            file_name = input("Enter file name: ")
            content = input("Enter content: ")
            write_to_file(file_name, content)
        elif choice == "7":
            file_name = input("Enter file name: ")
            view_file(file_name)
        elif choice == "8":
            file_name = input("Enter file name: ")
            delete_file(file_name)
        elif choice == "9":
            file_name = input("Enter file name: ")
            destination_folder = input("Enter destination folder: ")
            copy_file(file_name, destination_folder)
        elif choice == "10":
            file_name = input("Enter file name: ")
            destination_folder = input("Enter destination folder: ")
            move_file(file_name, destination_folder)
        elif choice == "11":
            old_name = input("Enter old file name: ")
            new_name = input("Enter new file name: ")
            rename_file(old_name, new_name)
        elif choice == "0":
            print("Exiting...")
            sys.exit()
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()

