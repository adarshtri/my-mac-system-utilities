# My Mac System Utilities

This project is all about those small utilities that you had always wished were their on your system 
(Mac support at present). 

## Top Features

1. Easy to configure

    All the utilities are easy to configure and control.
    
2. Utility level control

    All the utilities have individual control knobs in the configuration file. Just configure the things that 
    you want and the way you want them. Rest all can be set to inactive and they will never run.
    
3. Light weight
    
    No daemon processes or ever running threads are involved. The utilities run are automated with crontab. The
    project uses basic of python libraries under the hood.
    
4. Uses python (the best language in the world)
    
## Configuration File

The configuration file should be present under $HOME/.config/my-mac-system-utilities by the name "config.json".
The file initially contains default configuration which obviously should be altered to cater you purpose of using this
tool.

## Running the service in background

Clone this directory at some location on you system. Let us say that location is $HOME/utilities. Follow the following
steps to complete the setup of the services.

1. Clone this repository
2. Install requirements using `pip3 install -r $HOME/utilities/my-mac-system-utilities/requirements.txt`
3. Add an entry in crontab by following below commands

    a. crontab -e
    
    b. In the end add this line `*/5 * * * * python3 $HOME/utilities/my-mac-system-utilities/run.py`
    
    c. Alter the parameter */5 (this means run every five minutes) to whatever you feel is the best frequency to run these utilities.
4. And you are done :)


## Utilities supported

#### Battery Checker and alert manager
If you are always worried of hurting your laptop's battery by leaving it plugged
in this utility is for you. You can set minimum battery level to alert you to plugin the charger. And you can set maximum
battery level to get a alert to unplug charging.

    Configurations for battery checker
    
    `"battery_checker": { "active": true, "min": 25, "max": 95 }`
    
    active: `true` means this utility will run, `false` means it won't
    
    min: 25, this means the utility will notify you to plugin if your battery level is less than 25 and you are not plugged in
    
    max: 95, this means the utility will notify you to plug out if your battery level is more than 95 and you are plugged in

#### Directory cleaner and alert manager
If your "downloads" folder is always full of files with different and format and you
wished someone could automatically sort it based on file formats behind your back, this utility is for you. It manages everything
based on how you configure your directory cleaner in configuration file. It also gives you an alert on how many
files have been cleared up in each directory.

    Configurations for directory cleaner
        
    
        "directory_cleaner": {
            "active": true,
            "directories": {

                "/Users/atrivedi/Projects/tmp/": {
                    "format_directory_map": {
                        "pdf": "PDF",
                        "py": "Python",
                        "*": "other_format"
                    },
                    "active": true
                }
            }
        }
        
    a. The configurations for directory cleaner go under the key "directory_cleaner". 

    b. The "active" key under main "directory_cleaner" is to control the whole cleaner utility which when set to
    true will run the cleaner otherwise would skip running it.

    c. "directories" key specifies which all directories to watch for cleaning. 

    d. "format_directory_map" is the key which tells which all file formats to watch
    and where to put them once there is a new file with that format. So "pdf": "PDF" means if any .pdf file
    comes in /Users/atrived/Projects/tmp then it will be moved to /Users/atrived/Projects/tmp/PDF. 

    e. If you specify "*" in place of format, that means all other formats. So "*": "other_format" will put any file other than with extensions py and pdf to other_format directory of
    /Users/atrived/Projects/tmp.

    f. A directory level "active" configuration is provided to control every directory for cleanup.
    

#### Custom repeating and fixed time reminders
We all need reminding to do stuff which we can easily forget. This utility is just to solve this specific problem.
I build this reminders when I was doing my job search. It reminded me after every 30 minutes to open LinkedIn and
look through new openings and apply. I also used to daily remind me at 10AM to do leetcode.

    "custom_reminders": {
        "active": true,
        "reminders": {
          "repeating": {
            "45": [
              {
                "title": "Job Application",
                "subtitle": "Apply to new jobs.",
                "message": "Apply to jobs on LinkedIn.",
                "say": "It is now or never.",
                "active": true
              }
            ]
          },
          "fixed": {
            "14:00": [
              {
                "title": "Test Reminder",
                "subtitle": "This is a test reminder for fixed time.",
                "message": "This is hello from reminder tool.",
                "say": "This is hello from your reminder tool.",
                "active": true
              }
            ]
          }
        }
    }
    
You can configure two types of reminders, fixed time and repeating. Fixed type reminder is where you specify 
things which you want to get reminded at some fixed time of the day. Repeating reminders are reminders which 
triggers after every configured minutes. So for repeating reminders, a value of "15" means the reminder will 
trigger at 15, 30, 45, 00 minutes of every hour.

Every reminder needs to have five properties which are:

1. "title": Title of the reminder.
2. "subtitle": Subtitle of the reminder.
3. "message": Reminder message.
4. "say": The message that will be spoken by the system to you.
5. "active": Whether this reminder is active or not. If not active no notification is sent for that
particular reminder.
