import textutils.core as c

<<<<<<< HEAD
def test_reverse_words():
    text = "Hello World, my name is Jerico Agdan"
    assert c.reverse_words(text)
=======
def test_word_count_basic():
    text = "Cat dog cat"
    assert c.word_count(text) == {"cat": 2, "dog": 1}

def test_is_palindrome():
    text = "level"
    assert c.is_palindrome(text) == True

def test_average_word_length_basic():
    text = "Hello world! This is a test."
    assert c.average_word_length(text) == 23 / 6
>>>>>>> 912b13ac46d34a588963c46f0ca3a64d213a5159
