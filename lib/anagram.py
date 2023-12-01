# your code goes here!
class Anagram:
    def __init__(self, word, word_list=None):
        self.word = word
        self.word_list = word_list if word_list != None else list()
    def match(self, word_list=None):
        word_list = word_list if word_list != None else self.word_list
        anagram_list = list()

        for word in word_list:
            if (len(word) == len(self.word)) and (sorted(word) == sorted(self.word)):
                anagram_list.append(word)
        return anagram_list