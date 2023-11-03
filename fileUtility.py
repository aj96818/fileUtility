import os
import shutil
from datetime import datetime
import re

def organize_files(source_dir, destination_dir):
    total_files_processed = 0

    for root, _, files in os.walk(source_dir):
        for file in files:
            source_file_path = os.path.join(root, file)
            try:
                created_date = datetime.fromtimestamp(os.path.getmtime(source_file_path))
                month_year_folder = created_date.strftime("%Y-%m")
                month_year_path = os.path.join(destination_dir, month_year_folder)

                if not os.path.exists(month_year_path):
                    os.makedirs(month_year_path)

                if file.lower().endswith((".jpg", ".jpeg", ".png", ".gif", ".dng", ".tiff", ".tif", ".nef", ".cr2", ".psd", ".raw", ".heif", ".crw", ".3fr")):
                    destination_path = os.path.join(month_year_path, file)
                else:
                    if not os.path.exists(os.path.join(destination_directory, "Other")):
                        os.makedirs(os.path.join(destination_directory, "Other"))
                        destination_path = os.path.join(destination_directory, "Other", file)

                shutil.copy2(source_file_path, destination_path)
                total_files_processed += 1
            except Exception as e:
                print(f"Error copying {source_file_path}: {e}")

    print(f"Total files processed: {total_files_processed}")


def count_and_rename_dirs(destination_directory):
    for dirpath, dirnames, filenames in os.walk(destination_directory, topdown=False):
        # Calculate the total count of items (files and subdirectories)
        total_count = len(dirnames) + len(filenames)

        # Rename the current directory with the total count appended
        new_dirname = f"{os.path.basename(dirpath)}_Count_{total_count}"
        new_dirpath = os.path.join(os.path.dirname(dirpath), new_dirname)

        os.rename(dirpath, new_dirpath)


def delete_empty_dirs(destination_dir):
    for dirpath, dirnames, filenames in os.walk(destination_dir, topdown=False):
        # Check if the current directory is empty
        if not dirnames and not filenames:
            # Delete the empty directory
            os.rmdir(dirpath)
            print(f"Deleted empty directory: {dirpath}")    


if __name__ == "__main__":
    source_directory = "/Volumes/5TB ExFAT"
    destination_directory = "/Volumes/WD 5TB Mac/5TB ExFAT_SortedFiles"

    organize_files(source_directory, destination_directory)
    delete_empty_dirs(destination_directory)
    count_and_rename_dirs(destination_directory)
    
    # Calculate the new directory name by removing trailing digits and underscores
    new_destination_dir_name = re.sub(r"_\d+", "", os.path.basename(destination_directory))
    
    # Get the parent directory of the destination directory
    parent_directory = os.path.dirname(destination_directory)

    # Calculate the full path for the new directory
    new_destination_dir = os.path.join(parent_directory, new_destination_dir_name)

    # Check if the new directory name already exists
    # if not os.path.exists(new_destination_dir):
    #     try:
    #         # Rename the directory
    #         parent_dir = "/Volumes"
    #         all_items = os.listdir(parent_dir)
    #         pattern = r"Sorted Files*"
    #         matching_str = None
    #         for item in all_items:
    #             if re.match(pattern, item):
    #                 matching_str = item
    #                 break
    #         old_dest_dir_name = os.path.join(parent_dir, matching_str)
    #         os.rename(old_dest_dir_name, new_destination_dir)
    #         print(f"Sucessfully renamed: {old_dest_dir_name} to {new_destination_dir}")
    #     except OSError as e:
    #         print(f"Error renaming directory: {e}")
    # else:
    #     print(f"Error. Cannot rename directory. The directory '{new_destination_dir}' already exists.")
