import os
import shutil
from datetime import datetime

######### Helper Fns ######################## 

def create_directory(directory_path):
    # Ensure the directory exists
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

def move_file(source_path, destination_path):
    # Move the file to the destination folder
    shutil.move(source_path, destination_path)

def copy_file(source_path, destination_path):
    # Copy the file to the destination folder
    shutil.copy(source_path, destination_path)

def get_file_date(file_path, mode='created'):
    # Get the creation or modification date of the file
    if mode == 'created':
        timestamp = os.path.getctime(file_path)
    elif mode == 'modified':
        timestamp = os.path.getmtime(file_path)
    else:
        raise ValueError("Invalid mode. Use 'created' or 'modified'.")

    return datetime.fromtimestamp(timestamp).strftime("%b-%d-%Y")

###############################################

######## Organization Fns ########################################
    
def organize_files_by_date_and_extension(source_folder, destination_parent_folder, folder_prefix, extension):
    """
    Moves files with the specified extension created on the same date from the given source path to a new folder within 
    the destination_parent folder (if it doesn't already exist). 
    The new folder will be named {folder_prefix}_{current_date} for example 'RawVideoContent_Dec-10-2023'
    """

    # Ensure the destination parent folder exists
    create_directory(destination_parent_folder)

    # Iterate through files in the source folder
    for filename in os.listdir(source_folder):
        source_path = os.path.join(source_folder, filename)

        # Check if it's a file (not a subdirectory) and has the specified extension
        if os.path.isfile(source_path) and filename.lower().endswith(extension.lower()):

            # Get the file's date
            file_date = get_file_date(source_path)

            # Create the destination path based on the file extension
            destination_path = os.path.join(destination_parent_folder, f"{folder_prefix}_{file_date}")

            # Ensure the destination subfolder exists
            create_directory(destination_path)

            # Move the file to the destination folder
            move_file(source_path, destination_path)


def organize_files_by_name(source_folder, destination_parent_folder, keywords, folder_name=""):
    """
    Organize files with any of the given words in the keywords array in their name into a folder named folder_name. 
    For example, keywords "resume, cover, resumes" into resumes
    """
    # Ensure the destination parent folder exists
    create_directory(destination_parent_folder)

    # Iterate through files in the source folder
    for filename in os.listdir(source_folder):
        source_path = os.path.join(source_folder, filename)

        # Check if it's a file (not a subdirectory) and if the name contains any of the specified keywords
        if os.path.isfile(source_path) and any(keyword.lower() in filename.lower() for keyword in keywords):

            
            if folder_name != "":
                # Create the destination path based on the keyword
                destination_path = os.path.join(destination_parent_folder, folder_name)
            else:
                destination_path = destination_parent_folder

            # Ensure the destination folder exists
            create_directory(destination_path)

            # Move the file to the destination folder
            move_file(source_path, destination_path)

def organize_files_by_extensions(source_folder, destination_folder, extensions):
    """
    Moves files with any of the specified extensions to the destination folder. 
    """

    # Iterate through files in the source folder
    for filename in os.listdir(source_folder):
        source_path = os.path.join(source_folder, filename)

        # Check if it's a file (not a subdirectory) and has the specified extension
        if os.path.isfile(source_path) and any(filename.lower().endswith(extension.lower()) for extension in extensions):

            # Ensure the destination folder exists
            create_directory(destination_folder)

            destination_path = destination_folder

            # Move the file to the destination folder
            move_file(source_path, destination_path)


##############################################################


if __name__ == "__main__":
    #### This will organize my video content from my Downloads to put them on my External Hard Drive
    
    source_folder = "/Volumes/Macintosh HD/Users/matthewcruz/Downloads"
    destination_parent_folder = "/Volumes/Seagate /MattCruzFitness/Fitness Vids/RawVideos"

    organize_files_by_date_and_extension(source_folder, destination_parent_folder, "RawVideoContent", ".mov")


    #### This will organize the resumes I have in my Downloads folder into one Resume folder
    source_folder = "/Volumes/Macintosh HD/Users/matthewcruz/Downloads"
    destination_parent_folder = "/Volumes/Macintosh HD/Users/matthewcruz/Documents"

    organize_files_by_name(source_folder, destination_parent_folder, ["resume", "cover"],"Resumes")


    #### This will organize any meal plans and guide into one Meal Guides folder
    source_folder = "/Volumes/Macintosh HD/Users/matthewcruz/Downloads"
    destination_parent_folder = "/Volumes/Seagate /MattCruzFitness"
    organize_files_by_name(source_folder, destination_parent_folder, ["meal", "diet"],"MealGuides")

    #### This will add any updated versions of my logo into a Logo folder
    source_folder = "/Volumes/Macintosh HD/Users/matthewcruz/Downloads"
    destination_parent_folder = "/Volumes/Seagate /MattCruzFitness"
    organize_files_by_name(source_folder, destination_parent_folder, ["logo"],"Logos")

    #### This will move b reel downloads to their appropriate folder
    source_folder = "/Volumes/Macintosh HD/Users/matthewcruz/Downloads"
    destination_parent_folder = "/Volumes/Seagate /MattCruzFitness/FitnessVids/b-reel"
    organize_files_by_extensions(source_folder, destination_parent_folder, ["jpg","jpeg","gif","mp4"])


    #### This will add any miscellaneous fitness files into an appropriate folder
    source_folder = "/Volumes/Macintosh HD/Users/matthewcruz/Downloads"
    destination_parent_folder = "/Volumes/Seagate /MattCruzFitness"
    organize_files_by_name(source_folder, destination_parent_folder, ["fitness", "motivate","progressive", "testimonial", "muscle","belly","curvy","train","lift","strength","guide","tips"],"Misc")