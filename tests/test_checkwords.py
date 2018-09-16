import unittest
from checkwords import get_possible_words

class TestCheckWordsFunctions(unittest.TestCase):
  def test_get_possible_words(self):
    words = get_possible_words('flag')

    self.assertEqual(len(words), 9)

  def test_words_are_not_repeated(self):
    words = get_possible_words('ggood')
    no_duplicates = len(words) == len(set(words))

    self.assertTrue(no_duplicates)

if __name__ == '__main__':
  unittest.main()