import os
import psutil
from shutil import copyfile


# battery checker

def get_battery_status():
    
    # return the battery remaining
    
    battery = psutil.sensors_battery()
    return battery.percent


def is_battery_charging():
    
    # returns true is battery is charging
    # else returns false
    
    battery = psutil.sensors_battery()
    return battery.power_plugged


def should_plugin_battery_charging(minimum):
    
    # returns true if the battery should be plugged in for charging
    # else return False
    
    if get_battery_status() < minimum and not is_battery_charging():
        return True
    else:
        return False
    

def should_plug_out_battery_charging(maximum):
    
    # returns true if the battery is charged and
    # should be plugged out else return false
    
    if get_battery_status() > maximum and is_battery_charging():
        return True
    else:
        return False


def notify(title, text, subtitle):
    
    # create a system notification on mac
    
    os.system("""
              osascript -e 'display notification "{}" with title "{}" subtitle "{}" sound name "Ping"'
              """.format(text, title, subtitle))
    
    
def check_battery(config):
    
    # wrapper method to check for battery and create
    # suitable notification
    
    if config["active"]:
        if should_plugin_battery_charging(config["min"]):
            notify("Battery Alert", "Low battery. Plugin power.", "Below {}%".format(config["min"]))
        elif should_plug_out_battery_charging(config["max"]):
            notify("Battery Alert", "Battery charged. Plug out power.", "More than {}%".format(config["max"]))


# directory cleaner

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

            
def clean_directory(config):
    
    """
    This method is the wrapper method which is called from the run.py to clean directories as configured.
    :param config: The configuration for directory cleaning directory picked from config file.
    :return: None, should return exit status and based on that give a notification on desktop of successful or failed
    run.
    """
    
    if config["active"]:
        
        cleanup_directories = [x for x in config["directories"]]
        cleanup_directories = remove_missing_cleanup_directories(cleanup_directories)
        
        for directory in cleanup_directories:
            
            if config["directories"][directory]["active"]:
                create_missing_subdirectories_under_cleanup_directories(directory, config["directories"][directory])
                move_files_to_subdirectories(directory, config["directories"][directory])
