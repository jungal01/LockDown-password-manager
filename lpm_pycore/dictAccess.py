class DictAccess:
    """
    ============================================================================
    This class is simply to allow easier access to the dictionary. Use of this
    class will be restricted by the rest of the app to prevent abuse.

    addWord: allows either a single word or a group of words to be added to the
        dictionary. This function will throw a type error if the type isn't a
        string, list, set, or tuple.

    rmWord: allows either a single word or a group of words to be removed from
        the dictionary. This function will throw a type error if the type isn't
        a string, list, set, or tuple.

    readDict: closes the file and returns a set of the words in the dictionary
    ============================================================================
    """

    def __init__(self):
        self._f = open('dictionary.txt', 'r+')
        self._words = set(self._f.read().split('\n'))

    def addWord(self, word):
        if isinstance(word, str):
            self._words.add(word)
            self._f.write(word)

        elif isinstance(word, (list, set, tuple)):
            for i in word:
                self._words.add(i)
                self._f.write(i)

        else:
            raise TypeError("type {} cannot be added to file".format(type(word)))

    def rmWord(self, word):
        if isinstance(word, str):
            self._words.remove(word)
            self._f.seek(0)
            for i in self._words:
                if i != word:
                    self._f.write(i)
            self._f.truncate()

        elif isinstance(word, (list, set, tuple)):
            self._f.seek(0)
            for i in self._words:
                if i not in word:
                    self._f.write(i)
            self._f.truncate()

        else:
            raise TypeError("type {} cannot be removed from file".format(type(word)))

    def readDict(self):
        self._f.close()
        return self._words


def main():
    print(DictionaryAccess().readDict())

if __name__ == "__main__":
    main()
