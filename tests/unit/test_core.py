import textutils.core as c

def test_word_count_basic():
    text = "Cat dog cat"
    assert c.word_count(text) == {"cat": 2, "dog": 1}

def test_is_palindrome():
    text = "level"
    assert c.is_palindrome(text) == True

def test_average_word_length_basic():
    text = "Hello world! This is a test."
    assert c.average_word_length(text) == 23 / 6

def test_reverse_words():
    text = "Hello World, my name is Jerico"
    assert c.reverse_words(text)

def test_find_unique_words_basic():

    text = "Hello hello world"
    result = c.find_unique_words(text)
    assert result == {"hello", "world"}