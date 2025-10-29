import textutils.core as c

def test_word_count_basic():
    text = "Cat dog cat"
    assert c.word_count(text) == {"cat": 2, "dog": 1}

def test_is_palindrome():
    text = "level"
    assert c.is_palindrome(text) == True