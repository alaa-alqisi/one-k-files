import os
import sys
import shutil

def group_files_by_language(source_folder):
    # Get a list of all files in the source folder
    files = os.listdir(source_folder)
    
    # Create a dictionary to group files by language
    file_groups = {}
    for file in files:
        if file.endswith(".txt"):
            # Extract the language from the file name
            language, _ = file.split("-")

            # Create the destination folder for the language if it doesn't exist
            language_folder = os.path.join(source_folder, language)
            if language not in file_groups:
                file_groups[language] = True
                os.makedirs(language_folder, exist_ok=True)

            # Move the file to the respective language folder
            src_path = os.path.join(source_folder, file)
            dest_path = os.path.join(language_folder, file)
            shutil.move(src_path, dest_path)


    
source_folder = sys.argv[1]

if not source_folder:
    print("Usage: python script_name.py source_folder_path")
    sys.exit(1)

group_files_by_language(source_folder)
