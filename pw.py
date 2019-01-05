#! python3

#pw.py - An insecure password manager

#passwords are stored in a dictionary

PASSWORDS = {'email':"ZXCVqwer1234!@#$",
             'blog':"Y0urM0mBl0gs",
             'luggage':"12345"}

#sys.argv handles arguments, the first item should be the program name followed by the first argument

import sys,pyperclip
if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1] #first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account +'copied to clipboard.')
else:
    print("There is no account named " + account)



