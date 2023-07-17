# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    def is_anagram(self, word):
        return sorted(self.word.lower()) == sorted(word.lower())

    def match(self, word_list):
        return [word for word in word_list if self.is_anagram(word)]





