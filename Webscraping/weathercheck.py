"""
This script allows the user to check the weather for a specified location using the Time and Date website.
The location can be provided as a command-line argument.

Dependencies:
- webbrowser: To open web pages.
- sys: To handle command-line arguments.

Usage:
1. Run the script with the location as a command-line argument.
   Example: python weathercheck.py New York
"""

import webbrowser, sys

def check_weather():
   
    if len(sys.argv) > 1:
        location = ' '.join(sys.argv[1:])
        webbrowser.open("https://www.timeanddate.com/weather/?query=" + location)
    else:
        print("Please provide a location as a command-line argument.")
    


check_weather()