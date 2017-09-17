'''
================================================================================
Copyright 2017 Allen Junge

This file is part of Password Generator.
    Password Generator is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    any later version.
    
    Password Generator is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    
    You should have received a copy of the GNU General Public License
    along with Password Generator.  If not, see <http://www.gnu.org/licenses/>.
================================================================================
'''
import random
import hashlib


class PasswordGenerator:
    def __init__(self):
        try:
            dictionary = open('dictionary.txt')
            self.__words = set()
            for word in dictionary:
                self.__words.add(word.strip('\n'))
        except FileNotFoundError:
            raise Exception("Dictionary is missing, word passwords not possible")

        try:
            self.__used = open('usedpass.txt', "r+")
            self.__usedwords = set()
            for line in self.__used:
                self.__usedwords.add(line.strip("\n"))
        except FileNotFoundError:
            self.__used = open('usedpass.txt', 'w')
            self.__usedwords = set()

    def __Hash(self, item):
        item = item.encode('utf-8')
        return hashlib.sha3_512(item).hexdigest()

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
            char = [r.choice(lowletter), r.choice(lowletter), r.choice(upletter), r.choice(nums), r.choice(specialChar)]
            passwrd.append(r.choice(char))

        passwrd = ''.join(passwrd)
        if self.__Hash(passwrd) not in self.__usedwords:
            self.__used.write(self.__Hash(passwrd)+'\n')
            return passwrd

        else:
            self.randChars()

    def longRand(self):
        # repeat of randChars, with a higher char count
        # meant for more security
        r = random.SystemRandom()

        lowletter = list('abcdefghijklmnopqrstuvwxyz_')
        upletter = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        nums = list('1234567890')
        specialChar = list('!@#$%^&*()_\|/?{}')

        passwrd = []
        for x in range(r.randrange(16, 36)):
            char = [r.choice(lowletter), r.choice(lowletter), r.choice(upletter), r.choice(nums), r.choice(specialChar)]
            passwrd.append(r.choice(char))

        passwrd = ''.join(passwrd)
        if self.__Hash(passwrd) not in self.__usedwords:
            self.__used.write(self.__Hash(passwrd)+'\n')
            return passwrd

        else:
            self.longRand()

    def l33t(self, string):
        # meant to be called in case a password needs some nums
        # and special characters
        r = random.SystemRandom()
        l33tChars = {'a':'@','A':'4','e':'3','E':'3','i':'1','I':'!','o':'0','O':'0','b':'8','B':'8','g':'&','G':'&',
                     's':'5','S':'$','t':'7','T':'7','z':'2','Z':'2','l':'|','L':'1','h':'#','H':'#'}

        newleet = list(string)
        for x,y in enumerate(newleet):
            yn = r.choice([True,False])
            if yn:
                if y in l33tChars:
                    newleet[x] = l33tChars[y]

        return ''.join(newleet)

    def securePass(self):
        # has a maximum length of 35, using random choice
        # of 3-6 words with any length pulled from the dictionary.
        r = random.SystemRandom()
        passwrd = r.sample(self.__words, r.randrange(3,7))
        while len(''.join(passwrd)) > 35:
            passwrd = r.sample(self.__words,r.randrange(3,7))

        passwrd = ''.join(passwrd)
        if self.__Hash(passwrd) not in self.__usedwords:
            self.__used.write(self.__Hash(passwrd)+'\n')
            return passwrd

        else:
            self.securePass()

    def shortSecure(self):
        # has a char maximum of 18, and max 4 words
        r = random.SystemRandom()
        passwrd = r.sample(self.__words, r.randrange(2,5))
        while len(''.join(passwrd)) > 18:
            passwrd = r.sample(self.__words, r.randrange(2,5))

        passwrd = ''.join(passwrd)
        if self.__Hash(passwrd) not in self.__usedwords:
            self.__used.write(self.__Hash(passwrd)+'\n')
            return passwrd

        else:
            self.shortSecure()
