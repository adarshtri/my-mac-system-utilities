import psutil
import os


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
    
    if get_battery_status() <= minimum and not is_battery_charging():
        return True
    else:
        return False


def should_plug_out_battery_charging(maximum):
    # returns true if the battery is charged and
    # should be plugged out else return false
    
    if get_battery_status() >= maximum and is_battery_charging():
        return True
    else:
        return False
