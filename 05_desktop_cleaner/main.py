"""main.py
holds source code for desktop cleaner: program that sorts files in a dekstop folder 
by there file type automatically"""

import os
import shutil

def create_subfolder_if_needed(folder_path, subfolder_name):
    subfolder_path = os.path.join(folder_path, subfolder_name)

    if not os.path.exists(subfolder_path):
        os.makedirs(subfolder_path)
        
    return subfolder_path

def clean_folder(folder_path):
    for filename in os.listdir(folder_path):
        full_path = os.path.join(folder_path, filename)

        # Skip subfolders created by the script
        if not os.path.isfile(full_path):  
            continue

        # Get file extension
        file_extension = filename.split('.')[-1].lower()
        if file_extension:  # Ensure the file has an extension
            subfolder_name = f"{file_extension.upper()} Files"
            subfolder_path = create_subfolder_if_needed(folder_path, subfolder_name)
            
            new_location = os.path.join(subfolder_path, filename)
            if not os.path.exists(new_location):
                shutil.move(full_path, new_location)
                print(f"Moved: {full_path} ---> {new_location}")
            else:
                print(f"Skipped: {filename} as it already exists in {subfolder_path}")

if __name__ == "__main__":
    print("Desktop Cleaner Program")

    # Use a valid folder path
    folder_path = r'C:\Users\rrest\Downloads'
    
    if os.path.isdir(folder_path):
        clean_folder(folder_path)
        print("Cleaning complete")
    else:
        print(f"{folder_path} is an invalid folder path. Try again.")