'''
==================================
Copyright 2017 Allen Junge

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
==================================
'''
# This hastily written file is to split all the words
# in words.txt and place a single instance of each word
# into dictionary.txt for editing by the user and for
# reading by the main program
import re


def split_upper(s):
    return re.split("([A-Z][^A-Z]*)", s)


def main():
    unformatted = open('words.txt')
    newList = split_upper(unformatted.read())
    formattedWords = set()

    count = 0
    for x in newList:
        newList[count] = x.title()
        if '\n' not in newList[count]:
            newList[count] += '\n'
        formattedWords.add(newList[count])
        count += 1

    formattedWords.remove('\n')

    # convert to a list to make hand-editing easier
    formattedWords = list(formattedWords)
    formattedWords.sort()
    finalProduct = open("test.txt", 'w')
    for x in formattedWords:
        finalProduct.write(x)

    unformatted.close()
    finalProduct.close()

if __name__ == "__main__":
    main()

