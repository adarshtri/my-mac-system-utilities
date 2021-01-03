import os
import shutil
import functools
import json


def configuration_directory_exist():
    
    # check if the configuration directory exists in the
    # home directory of the user
    
    home = os.getenv("HOME", None)
    
    if not home:
        return False
    
    configuration_directory = home + "/.config/my-mac-system-utilities/"
    
    return os.path.isdir(configuration_directory)


def get_configuration_directory():
    
    home = os.getenv("HOME", None)
    return home + "/.config/my-mac-system-utilities/"


def get_configuration_file():
    return get_configuration_directory() + "/config.json"


def configuration_file_exist():
    
    if configuration_directory_exist():
        if "config.json" in os.listdir(get_configuration_directory()):
            return True
    
    return False


def create_missing_configuration_directory():
    
    if not configuration_directory_exist():
        os.makedirs(get_configuration_directory())


def copy_default_configuration():
    shutil.copyfile(os.getcwd() + "/config.json", get_configuration_directory() + "/config.json")
    

def get_configuration():
    
    configuration_file = get_configuration_file()
    
    with open(configuration_file, 'r') as fp:
        try:
            conf = json.load(fp)
        except json.JSONDecodeError:
            conf = None
    
    return conf
    

def handle_configuration():
    
    if not configuration_directory_exist():
        create_missing_configuration_directory()
    
    if not configuration_file_exist():
        copy_default_configuration()


def handle_config(func):
    @functools.wraps(func)
    def wrapper_handle_config(*args, **kwargs):
        handle_configuration()
        func(*args, **kwargs)
    return wrapper_handle_config
