import os
from shutil import copyfile
from lib.commonlib import notify


def remove_missing_cleanup_directories(directories: list) -> list:
    """
    This method take a list of directories and returns a new list with invalid or non-existing directories
    removed from the original list.
    :param directories: Directories to be checked for existence.
    :return: Updated list of directories.
    """
    
    for directory in directories:
        if os.path.isdir(directory):
            yield directory


def create_missing_subdirectories_under_cleanup_directories(cleanup_directory, directory_config):
    """
    This method creates the sub directories that should exist under cleanup directories where the files are moved to.
    :param cleanup_directory: The base cleanup directory.
    :param directory_config: Specific cleanup directory config.
    :return: None
    """
    
    for file_format in directory_config["format_directory_map"]:
        
        sub_directory = cleanup_directory + "/" + directory_config["format_directory_map"][file_format]
        
        if not os.path.isdir(sub_directory):
            os.makedirs(sub_directory)


def move_files_to_subdirectories(cleanup_directory, directory_config):
    """
    This method moves files from cleanup directory to sub directories based on file format and
    final directory configuration. It also creates a notification for number of files cleared
    in the cleanup directory.
    :param cleanup_directory: The base cleanup directory.
    :param directory_config: The configuration for the cleanup directory.
    :return: None
    """
    
    # get only files in the cleanup directory
    files_in_cleanup_directory = [os.path.join(cleanup_directory, f) for f in os.listdir(cleanup_directory)
                                  if os.path.isfile(os.path.join(cleanup_directory, f))]
    
    format_directory_map = directory_config["format_directory_map"]
    
    files_moved = 0
    
    for f in files_in_cleanup_directory:
        
        # get the format of the file
        file_format = f.split("/")[-1].split(".")[-1]
        
        # if the format is configured then copy the file to destination and remove it from source
        if file_format in format_directory_map:
            copyfile(f, os.path.join(cleanup_directory, format_directory_map[file_format], f.split("/")[-1]))
            os.remove(f)
            files_moved += 1
        elif "*" in format_directory_map:
            copyfile(f, os.path.join(cleanup_directory, format_directory_map["*"], f.split("/")[-1]))
            os.remove(f)
            files_moved += 1
    
    if files_moved > 0:
        notify("Directory Cleaner", cleanup_directory, "Cleared {} files.".format(files_moved))