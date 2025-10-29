import textutils.core as c

def test_remove_punctuation_basic():
    text = "Hello, world!"
    assert c.remove_punctuation(text) == "Hello world"

def test_empty_string():
    assert count_vowels("") == 0

def test_no_vowels():
    assert count_vowels("bcdfg") == 0

def test_all_vowels():
    assert count_vowels("aeiouAEIOU") == 10

def test_mixed_characters():
    assert count_vowels("Hello World!") == 3

def test_numerals_and_symbols():
    assert count_vowels("1234!@#$") == 0
    
def test_capitalize_sentences_basic():
    text = "hello world. this is a test! is it working?"
    expected = "Hello world. This is a test! Is it working?"
    assert c.capitalize_sentences(text) == expected



