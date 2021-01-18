from lib.commonlib import notify, get_current_time_parameters
import shutil


def check_space(config):
    """
    This is the template method which calls all the required methods for space checking and alert generation.
    :param config: The config.json configuration.
    :return: None, ideally should return run status
    """
    limit = config["show_alert_when_less_than"]
    
    total, used, free = get_usage()
    
    if free < limit:
        notify("Space Checker",
               "Low space on hard disk.",
               "Your space left on hard disk is less than {}GiB.".format(limit))
        
    if config["show_space_alert"]:
        
        current_time = get_current_time_parameters()
        
        configured_hour, configured_minute = config["show_space_alert_at"].split(":")
        configured_hour = int(configured_hour)
        configured_minute = int(configured_minute)
        
        if configured_hour == current_time["hour"] and configured_minute == current_time["minute"]:
            notify("Space Checker",
                   "Space usage alert.",
                   "Free space: {}GiB".format(free))


def get_usage():
    
    total, used, free = shutil.disk_usage("/")
    
    total = total // (2**30)
    used = used // (2**30)
    free = free // (2**30)
    
    return total, used, free
