import os
import psutil


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


def should_plugin_battery_charging():
    
    # returns true if the battery should be plugged in for charging
    # else return False
    
    if get_battery_status() < 25 and not is_battery_charging():
        return True
    else:
        return False
    

def should_plug_out_battery_charging():
    
    # returns true if the battery is charged and
    # should be plugged out else return false
    
    if get_battery_status() == 100 and is_battery_charging():
        return True
    else:
        return False


def notify(title, text):
    
    # create a system notification on mac
    
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))
    
    
def check_battery():
    
    # wrapper method to check for battery and create
    # suitable notification

    if should_plugin_battery_charging():
        notify("Battery Alert", "Low battery. Plugin power.")
    elif should_plug_out_battery_charging():
        notify("Battery Alert", "Battery charged. Plug out power.")
