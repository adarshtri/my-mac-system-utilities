from lib.dig_git import dig
from lib.battery_checker import *
from lib.directory_cleaner import *
from lib.custom_reminders import remind
    
    
def check_battery(config):
    
    # wrapper method to check for battery and create
    # suitable notification
    
    if config["active"]:
        if should_plugin_battery_charging(config["min"]):
            notify("Battery Alert", "Low battery. Plugin power.", "Below {}%".format(config["min"]))
        elif should_plug_out_battery_charging(config["max"]):
            notify("Battery Alert", "Battery charged. Plug out power.", "More than {}%".format(config["max"]))

            
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


def dig_git(config):
    
    """
    This method is a wrapper method which is called run.py to dig git repositories from the configured root
    directory.
    :param config: The configuration for git dig is picked from config file.
    :return: None, should return exit status and based on that give a notification on desktop of successful or failed
    run.
    """
    
    if config["active"]:
        dig(config=config)


def custom_reminders(config):
    
    """
    This method is a wrapper method which is called by run.py to look for all the pending reminders.
    :param config: The configuration for reminder notifications picked from config file.
    :return: None, should return exit status based on run status, give a notification of successful run or failure.
    """
    
    remind(config=config)
