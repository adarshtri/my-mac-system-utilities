import os
import datetime


def notify(title, text, subtitle, say=None):
    
    """
    This method creates a notification on mac systems. The notification can have a title, subtitle and the message
    text. Along with showing notification, if you want your system to speak up a message to you pass that in the "say"
    parameter and your system will notify you with the speech as well.
    :param title: Title of the notification.
    :param text: Text/main message of the notification.
    :param subtitle: Subtitle of the message.
    :param say: The message to be spoken by the system to you.
    :return: None
    """
    
    os.system("""
              osascript -e 'display notification "{}" with title "{}" subtitle "{}" sound name "Ping"'
              """.format(text, title, subtitle, text))
    
    if say:
        os.system("""
                osascript -e 'say "{}"'
                """.format(say))


def get_current_time_parameters():
    
    """
    This is a helper function which returns parameters of current time in dictionary.
    :return: current time parameters.
    """
    
    current_time = datetime.datetime.now()
    
    return {
        "day": current_time.day,
        "month": current_time.month,
        "year": current_time.year,
        "hour": current_time.hour,
        "minute": current_time.minute,
        "second": current_time.second
    }
