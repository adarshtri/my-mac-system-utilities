import datetime
from lib.commonlib import notify


def send_repeating_reminders(repeating_reminder_config: dict) -> None:
    """
    This method sends all the repeating reminders, that for now supports just repeating minutes.
    :param repeating_reminder_config: The configuration for repeating reminders picked from the config file.
    :return: None
    """
    for key in repeating_reminder_config:
        for repeating_reminder in repeating_reminder_config[key]:
            if repeating_reminder["active"]:
                try:
                    minute = int(key)
                    if 0 < minute < 60:
                        current_time = datetime.datetime.now()
                        current_minute = int(current_time.minute)
                        
                        if current_minute % minute == 0 and current_minute != 0:
                            notify(title=repeating_reminder["title"],
                                   text=repeating_reminder["message"],
                                   subtitle=repeating_reminder["subtitle"],
                                   say=repeating_reminder["say"])
                except ValueError as e:
                    pass


def send_fixed_reminders(fixed_reminder_config: dict) -> None:
    """
    This method sends all the fixed time reminders.
    :param fixed_reminder_config: The configuration for fixed reminders picked from the config file.
    :return: None
    """
    
    for key in fixed_reminder_config:
        for fixed_reminder in fixed_reminder_config[key]:
            if fixed_reminder["active"]:
                
                try:
                    hour, minute = key.split(":")
                    try:
                        
                        hour = int(hour)
                        minute = int(minute)
                        
                        if -1 < hour < 24 and -1 < minute < 60:
                            
                            current_time = datetime.datetime.now()
                            current_hour = int(current_time.hour)
                            current_minute = int(current_time.minute)
                            
                            if current_hour == hour and current_minute == minute:
                                
                                notify(title=fixed_reminder["title"],
                                       subtitle=fixed_reminder["subtitle"],
                                       text=fixed_reminder["message"],
                                       say=fixed_reminder["say"])
                    except ValueError as e:
                        pass
                except ValueError as ve:
                    pass
                        
            
def remind(config: dict) -> None:
    """
    The wrapper function to send reminders.
    :param config: Configuration for custom reminders, picked from config file.
    :return: None
    """
    
    send_repeating_reminders(config["reminders"]["repeating"])
    send_fixed_reminders(config["reminders"]["fixed"])
