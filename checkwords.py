from nltk.corpus import words
from itertools import permutations, combinations

def get_possible_words(letters):
  '''
  This function arranges the letters in all possible ways,
  checks each arrangement if it's an English word
  and adds it to a list which it returns after the operation.
  '''
  possible_words = []

  for i in range(2, len(letters) + 1):
    for c in combinations(letters, i):
      for p in permutations(''.join(c)):
        potential_word = ''.join(p)
        if potential_word in words.words():
          possible_words.append(potential_word)

  return possible_words
