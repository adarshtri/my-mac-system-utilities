from conf_lib import get_configuration, handle_config
from util_lib import notify, check_battery


@handle_config
def run():
    configuration = get_configuration()
    
    if not configuration:
        notify("My System Mac Utilities", "Configuration set improperly.")
        exit(1)
    
    if configuration["battery_checker"]["active"]:
        check_battery()


if __name__ == "__main__":
    
    run()
