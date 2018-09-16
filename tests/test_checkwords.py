import unittest
from checkwords import check, get_possible_words

class TestCheckWordsFunctions(unittest.TestCase):
  def test_check(self):
    self.assertTrue(check('soup'))

  def test_get_possible_words(self):
    possible_words = get_possible_words('flag')
    words = ['fa', 'la', 'al', 'ga', 'alf', 'fag', 'lag', 'gal', 'flag']

    self.assertEqual(possible_words, words)

if __name__ == '__main__':
  unittest.main()