# your code goes here!
class Anagram:
  def __init__(self, word):
    self.word = word

  def match(self, list):
    wordlist = []

    first_word = [letter for letter in self.word]
    first_word.sort()

    for word in list:
      second_word = [letter for letter in word]
      second_word.sort()

      if first_word == second_word:
        wordlist.append(word)

    self.list = wordlist
    return wordlist




