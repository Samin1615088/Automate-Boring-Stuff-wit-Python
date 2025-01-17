import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    #Get address from the command-line
    address = ' '.join(sys.argv[1:])
else:
    # Get address from the clipboard
    address = pyperclip.paste()

#TODO: Get address from clipboard
webbrowser.open('https://www.google.com/maps/place/' + address)


