# textutils-1

textutils

A small collaborative Python package that provides simple text utilities for text cleaning, analysis, and word operations.

Installation

Clone the repository:

git clone https://github.com/BorisaAlargic-cyber/textutils-1.git
cd textutils-1

Create and activate the environment (using micromamba):

micromamba create -f environment.yml -y
micromamba activate textutils

Install the package in editable mode:

pip install -e .

Running Tests

To run all tests and check coverage:

pytest

To see detailed coverage information:

pytest --cov=src/textutils --cov-report=term-missing

Features

remove_punctuation(text) → removes all punctuation from a string

count_vowels(text) → counts the number of vowels in the given text

capitalize_sentences(text) → capitalizes the first letter of each sentence

word_lengths(text) → returns a dictionary mapping each word to its length

is_anagram(a, b) → checks if two strings are anagrams (ignores case and punctuation)

is_palindrome(text) → checks if a string reads the same forwards and backwards

word_count(text) → counts the frequency of each word in a text

average_word_length(text) → calculates the average word length in the text

reverse_words(text) → reverses the order of words in a sentence

find_unique_words(text) → returns the set of unique words from the text

Team
Name GitHub Username

Borisa Alargic BorisaAlargic-cyber

Sabeena Awan sabeenaawan-del

Jerico Neil Agdan JericoNeil

Lorenzo Giovanni Costa Lorenzo-Costa-Git

Sara Saleem sarasaleem1997
