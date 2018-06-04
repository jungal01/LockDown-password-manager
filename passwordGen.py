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
import random


class PasswordGenerator:
    """
    ============================================================================
    This is the password generating class. It has 5 methods. At the moment, it
    uses random.SystemRandom to generate crypto secure randomness, but this
    dependency means it may not work on every system.
    
    randChars: creates a password of between 8 and 16 random chars. Intended
        for creating a quick, unique password for one time use.
        
    longRand: creates a password of between 16 and 52 random chars. Intended
        for creating a quick password that is meant for less important things,
        but needs to be used on a service more than one time.
        
    l33t: This is an internal method, designed to make passwords palatable to
        archaic systems that require numbers and symbols. In the future, it 
        will have a percentage of leeting.
        
    securePass: This is the most secure generator. It uses between 3
        and 10 words, has no upper limit, and has a lower limit of 26 chars.
        
    shortSecure: This is generally more secure than the random generators, but
        still inferior to securePass. To get past ridiculous password length
        limits, this method uses between 2 and 5 words, and has an upper limit
        of 18 chars.
    ----------------------------------------------------------------------------
    I believe I should explain some implementation details. The randomness is
    created in every method call to prevent a predictable password to be
    generated between multiple uses of the same class instance. I chose to name
    munge the dictionary set to protect from attackers changing the dictionary
    without editing the code by hand.
    ============================================================================
    """
    def __init__(self, passwrd=None, leetIt=False):
        try:
            dictionary = open('dictionary.txt')
            self.__words = set()
            for word in dictionary:
                self.__words.add(word.strip('\n'))
        except FileNotFoundError:
            raise Exception("Dictionary is missing, word passwords not possible")

    def randChars(self):
        r = random.SystemRandom()
        # sets up all the preferred characters
        lowletter = list('abcdefghijklmnopqrstuvwxyz_')
        upletter = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        nums = list('1234567890')
        specialChar = list('!@#$%^&*()_\|/?{}')

        passwrd = []
        for x in range(r.randrange(8, 17)):
            # lowletter is used twice to add a password-like balance
            char = [r.choice(lowletter), r.choice(lowletter), 
                    r.choice(upletter), r.choice(nums), r.choice(specialChar)]
            passwrd.append(r.choice(char))

        return ''.join(passwrd)

    def longRand(self):
        # repeat of randChars, with a higher char count
        # meant for more security
        r = random.SystemRandom()

        lowletter = list('abcdefghijklmnopqrstuvwxyz_')
        upletter = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        nums = list('1234567890')
        specialChar = list('!@#$%^&*()_\|/?{}')

        passwrd = []
        for x in range(r.randrange(16, 53)):
            char = [r.choice(lowletter), r.choice(lowletter),
                    r.choice(upletter), r.choice(nums), r.choice(specialChar)]
            passwrd.append(r.choice(char))

        return ''.join(passwrd)

    def l33t(self, string):
        # meant to be called in case a password needs some nums and special
        # characters
        r = random.SystemRandom()
        l33tChars = {'a':'@','A':'4','e':'3','E':'3','i':'1','I':'!','o':'0',
                     'O':'0','b':'8','B':'8','g':'&','G':'&','s':'5','S':'$',
                     't':'7','T':'7','z':'2','Z':'2','l':'|','L':'1','h':'#',
                     'H':'#'}

        newleet = list(string)
        for x,y in enumerate(newleet):
            yn = r.choice([True,False])
            if yn:
                if y in l33tChars:
                    newleet[x] = l33tChars[y]

        return ''.join(newleet)

    def securePass(self):
        # This is creates a far more secure password. There is no real upper 
        # limit on size. It will pull at least 3 and up to 10 words from the set
        r = random.SystemRandom()
        passwrd = ''.join(r.sample(self.__words, r.randrange(3,10)))
        print(len(passwrd) < 25) 
        while len(passwrd) < 25:
            passwrd = ''.join(r.sample(self.__words, r.randrange(3,10)))

        return ''.join(passwrd), len("".join(passwrd))

    def shortSecure(self):
        # has a char maximum of 18, and max 4 words
        r = random.SystemRandom()
        passwrd = r.sample(self.__words, r.randrange(2,5))
        while len(''.join(passwrd)) > 18:
            passwrd = r.sample(self.__words, r.randrange(2,5))

        return ''.join(passwrd), len("".join(passwrd))


def main():
    usr = input("(s)hort (l)ong (q)uit: ")
    passwrd = PasswordGenerator()
    while usr != ('q' or 'quit'):
        if usr == ('s' or 'short'):
            print(passwrd.shortSecure())
        elif usr == ('l' or 'long'): 
            print(passwrd.securePass())

        usr = input("(s)hort (l)ong (q)uit: ")

if __name__=="__main__":
    main()