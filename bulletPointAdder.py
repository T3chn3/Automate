#! python3
#bulletPointAdder.py - Adds Wikipedia bullet points to the start of each line of text on the clipboard

'''
1) paste text from the clipboard
2) modify the text
3) copy the modified text back to the clipboard
'''

import pyperclip
#1
text = pyperclip.paste()

#2
# TODO: Separate lines and add stars
# Debug: print(text)
lines = text.split('\n')
for i in range(len(lines)):   #loop through all indexes in the "lines" list
    lines[i] = '* ' + lines[i] #adding the start
text = '\n'.join(lines)

#3
pyperclip.copy(text)

'''
Contents of buffer prior to script execution:
Lists of advertising characters
Lists of characters from The Office
Lists of Coronation Street characters
Lists of CSI characters
Lists of Emmerdale characters
Lists of fictional Presidents of the United States
Lists of Hollyoaks characters

Contents of buffer after script execution:
* Lists of advertising characters
* Lists of characters from The Office
* Lists of Coronation Street characters
* Lists of CSI characters
* Lists of Emmerdale characters
* Lists of fictional Presidents of the United States
* Lists of Hollyoaks characters
'''