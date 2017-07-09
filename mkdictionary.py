'''
==================================
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
==================================
'''

# I couldn't figure it out, but despite the set filtering most repeats,
# The only way to get exactly one instance of each word is to run this
# twice, replacing 'words.txt' with 'dictionary.txt'

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

    formattedWords.remove('\n')

    formattedWords = list(formattedWords)
    formattedWords.sort()
    finalProduct = open("dictionary.txt", 'w')
    for x in formattedWords:
        finalProduct.write(x)

    unformatted.close()
    finalProduct.close()

main()
