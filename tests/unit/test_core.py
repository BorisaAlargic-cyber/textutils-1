import textutils.core as c

def test_remove_punctuation_basic():
    text = "Hello, world!"
    assert c.remove_punctuation(text) == "Hello world"

def test_empty_string():
    assert c.count_vowels("") == 0

def test_no_vowels():
    assert c.count_vowels("bcdfg") == 0

def test_all_vowels():
    assert c.count_vowels("aeiouAEIOU") == 10

def test_mixed_characters():
    assert c.count_vowels("Hello World!") == 3

def test_numerals_and_symbols():
    assert c.count_vowels("1234!@#$") == 0
    
def test_capitalize_sentences_basic():
    text = "hello world. this is a test! is it working?"
    expected = "Hello world. This is a test! Is it working?"
    assert c.capitalize_sentences(text) == expected

def test_word_lengths_basic():
    result = c.word_lengths("Hello world")
    assert result == {"hello": 5, "world": 5}


def test_is_anagram_true():
    assert c.is_anagram("listen", "silent")
    assert c.is_anagram("Dormitory", "dirty room")
    assert c.is_anagram("Astronomer", "Moon starer")
    assert c.is_anagram("The eyes", "They see")

def test_is_anagram_false():
    assert not c.is_anagram("hello", "world")
    assert not c.is_anagram("python", "typhonx")
    assert not c.is_anagram("test", "taste")


