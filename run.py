from lib.conf_lib import get_configuration, handle_config, get_configuration_file
from lib.util_lib import notify, check_battery, clean_directory, dig_git, custom_reminders, space_checker


@handle_config
def run():
    configuration = get_configuration()
    
    if not configuration:
        notify("My System Mac Utilities", "Check configuration file at {}".format(get_configuration_file()),
               "Configuration set improperly")
        exit(1)
    
    if configuration["battery_checker"]["active"]:
        check_battery(get_configuration()["battery_checker"])
        
    if configuration["directory_cleaner"]["active"]:
        try:
            clean_directory(configuration["directory_cleaner"])
        except PermissionError as pe:
            pass
        
    if configuration["git_digger"]["active"]:
        dig_git(config=configuration["git_digger"])
        
    if configuration["custom_reminders"]["active"]:
        custom_reminders(config=configuration["custom_reminders"])
        
    if configuration["space_checker"]["active"]:
        space_checker(config=configuration["space_checker"])


if __name__ == "__main__":
    run()
