import os
import shutil
from datetime import datetime

def create_directory(directory_path):
    # Ensure the directory exists
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

def move_file(source_path, destination_path):
    # Move the file to the destination folder
    shutil.move(source_path, destination_path)

if __name__ == "__main__":
    # Replace these paths with your actual source and parent destination folders
    source_folder = "/path/to/source/folder"
    destination_parent_folder = "/path/to/destination/parent/folder"

    # Organize files by extension (e.g., move all .txt files to the folder with a custom name including text and the current date)
    organize_files_by_extension(source_folder, destination_parent_folder, ".txt")
