from conf_lib import get_configuration, handle_config, get_configuration_file
from util_lib import notify, check_battery


@handle_config
def run():
    configuration = get_configuration()
    
    if not configuration:
        notify("My System Mac Utilities", "Check configuration file at {}".format(get_configuration_file()),
               "Configuration set improperly")
        exit(1)
    
    if configuration["battery_checker"]["active"]:
        check_battery(get_configuration()["battery_checker"]["min"], get_configuration()["battery_checker"]["max"])


if __name__ == "__main__":
    run()
