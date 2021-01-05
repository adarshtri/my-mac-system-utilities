from lib.conf_lib import get_configuration, handle_config, get_configuration_file
from lib.util_lib import notify, check_battery, clean_directory


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
        clean_directory(configuration["directory_cleaner"])


if __name__ == "__main__":
    run()
