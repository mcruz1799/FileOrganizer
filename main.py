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
    
def organize_files_by_extension(source_folder, destination_parent_folder, folder_prefix, extension):
    # Get the current date
    current_date = datetime.now().strftime("%b-%d-%Y")

    # Create the destination folder with a custom name including text and the current date
    destination_folder = os.path.join(destination_parent_folder, f"{folder_prefix}_{current_date}")

    # Ensure the destination folder exists
    create_directory(destination_folder)

    # Iterate through files in the source folder
    for filename in os.listdir(source_folder):
        source_path = os.path.join(source_folder, filename)

        # Check if it's a file (not a subdirectory) and has the specified extension
        if os.path.isfile(source_path) and filename.endswith(extension):
            # Determine the destination path based on the file extension
            destination_path = os.path.join(destination_folder, filename)

            # Ensure the destination subfolder exists
            create_directory(destination_folder)

            # Move the file to the destination folder
            move_file(source_path, destination_path)
            
if __name__ == "__main__":
    # Replace these paths with your actual source and parent destination folders
    source_folder = "/path/to/source/folder"
    destination_parent_folder = "/path/to/destination/parent/folder"

    # Organize files by extension (e.g., move all .txt files to the folder with a custom name including text and the current date)
    organize_files_by_extension(source_folder, destination_parent_folder, ".txt")
