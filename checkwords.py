from nltk.corpus import words
from itertools import permutations, combinations
from typeguard import typechecked

word_set = set(words.words())

@typechecked
def get_possible_words(letters: str) -> list:
  '''
  This function arranges the letters in all possible ways,
  checks each arrangement if it's an English word
  and adds it to a list which it returns after the operation.
  '''
  possible_words = []

  for i in range(2, len(letters) + 1):
    letter_combinations = set(combinations(letters, i))

    for c in letter_combinations:
      unique_permutations = set(permutations(''.join(c)))

      for p in unique_permutations:
        word = ''.join(p)
        if word in word_set and word not in set(possible_words):
          possible_words.append(word)

  return possible_words
