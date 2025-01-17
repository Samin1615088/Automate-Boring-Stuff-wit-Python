"""
This script allows the user to search for a location on Google Maps using two methods:
1. By providing an address via the clipboard or command-line input.
2. By reading addresses from a file named 'location.txt' (or any file user created).

The user is prompted to choose one of the methods, and the script will open the corresponding
Google Maps search results in the default web browser.

Dependencies:
- webbrowser: To open web pages.
- sys: To handle command-line arguments.
- pyperclip: To read from the clipboard.
- time: To add delays between opening multiple addresses from a file.

Usage:
1. Run the script.
2. Choose the method to search for the location.
"""


import webbrowser, sys, pyperclip, time

# function to search location by clipboard or input
def search_location_from_clipboard_or_input():
    if len(sys.argv) > 1:
        #Get address from the command-line
        address = ' '.join(sys.argv[1:])
    else:
        # Get address from the clipboard
        address = pyperclip.paste()
    #Get address from clipboard
    webbrowser.open('https://www.google.com/maps/place/' + address)
 

def search_location_from_file():
    file = open('location.txt', 'r')
    addresslist = file.readlines()
    file.close()
    
    for address in addresslist:
        webbrowser.open('https://www.google.com/maps/place/' + address)
        time.sleep(1)



# Prompt user to choose method
choice = input("Choose method to search location:\n"
               + "1: Clipboard/Input\n"
               + "2: File\n")

if choice == '1':
    # search by clipboard or input
    search_location_from_clipboard_or_input()
elif choice == '2':
    # search by file
    search_location_from_file()
else:
    print("Invalid choice. Please enter 1 or 2.")
