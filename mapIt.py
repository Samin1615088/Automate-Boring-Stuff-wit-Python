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
