## Checkwords

Check word is a script used to check all possible English words in a given string of letters.

### Installation

First of all you should clone this repository:
```
$ git clone https://github.com/otseobande/checkwords
```
This script uses the nltk library so to get things started we have to install it:
```
$ pip install nltk
```
After the installing nltk you need to download the __words__ corpus.
```
$ python
>>> nltk.download('words')
```
You should be good to go.

### Usage

```
>>> from checkwords.checkwords import get_possible_words
>>> get_possible_words('flag')
['fa', 'la', 'al', 'ga', 'alf', 'fag', 'lag', 'gal', 'flag']

```

### Testing

To run tests simply use:

```
$ python -m unittest discover -v
```

#### License and Copyright

Licensed under the [MIT License](LICENSE).