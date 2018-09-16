from nltk.corpus import words
from itertools import permutations, combinations

def check(word):
  return word in words.words()

def get_possible_words(letters):
  possible_words = []

  for i in range(2, len(letters) + 1):
    for c in combinations(letters, i):
      for p in permutations(''.join(c)):
        potential_word = ''.join(p)
        if check(potential_word):
          possible_words.append(potential_word)

  return possible_words
