'''
================================================================================
Copyright 2017-2018 Allen Junge

This file is part of LockDown.
    LockDown is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    any later version.
    
    LockDown is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    
    You should have received a copy of the GNU General Public License
    along with LockDown.  If not, see <http://www.gnu.org/licenses/>.
================================================================================
'''
#!/usr/bin/env python3


import sys
import passwordGen


# gen, store, and launch are the cli options. Gen will create a specified
# password type, store will prompt the user for a password and then store the
# password in the password file, and launch will run the gui. Future plans
# involve storing the ramdomly created password. Launch will be the default.
# g==gen, s==store, l==launch
gen = False
store = False
launch = True

# this will stop the gui from launching if other options are passed
if len(sys.argv) > 1 and sys.argv[1][0] == '-':
    launch = False

# this turns on the cli options. Launch should be incompatible with the others.
for arg in sys.argv:
    if arg[0] == '-':
        if 'g' in arg:
            gen = True
        if 's' in arg:
            store = True
        elif 'l' in arg:
            launch = True
            
def storePass(passwrd):
    # this function handles all the things necessary to store passwords
    pass


def launchApp():
    # this function isn't exactly necessary, but it helps me know what needs to 
    # get done.
    pass


def genPass(passType):
    # this calls the password generator class in passwordGen. The password types
    # are: sr==randChars, lr==longRand, sw==shortSecure, lw==securePass
    passwrd = passwordGen.PasswordGenerator()
    if passType == 'sr':
        return passwrd.shortChars()
    elif passType == 'lr':
        return passwrd.longRand()
    elif passType == 'sw':
        return passwrd.shortSecure()
    elif passType == 'lw':
        return passwrd.securePass()
    else:
        raise TypeError("That is not a password option!")
    

passType = ''
if sys.argv[1][0] != '-':
    passType = sys.argv[1]

if gen and store:
    