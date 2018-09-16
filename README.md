# Checkwords

Check word is a script used to check all possible English words in a given string of letters.

### Installation

First of all you should clone this repository and navigate into the project folder:

```
$ git clone https://github.com/otseobande/checkwords
$ cd checkwords
```

Then you need to install the dependencies:

```
$ pip install -r requirements.txt
```

After the installing dependencies download the __words__ corpus.

```
$ python
>>> nltk.download('words')
```

You should be good to go.

### Usage

```
>>> from checkwords import get_possible_words
>>> get_possible_words('flag')
['fa', 'la', 'al', 'ga', 'alf', 'fag', 'lag', 'gal', 'flag']
>>>
```

### Testing

To run tests simply run:

```
$ python -m unittest discover -v
```

#### License and Copyright

Licensed under the [MIT License](LICENSE).