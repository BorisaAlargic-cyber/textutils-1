import textutils.core as c

def test_capitalize_sentences_basic():
    text = "hello world. this is a test! is it working?"
    expected = "Hello world. This is a test! Is it working?"
    assert c.capitalize_sentences(text) == expected

def test_capitalize_sentences_single_sentence():
    text = "python is fun"
    expected = "Python is fun"
    assert c.capitalize_sentences(text) == expected

def test_capitalize_sentences_empty():
    assert c.capitalize_sentences("") == ""

def test_capitalize_sentences_spaces():
    text = "   hello world   .  how are you?   "
    expected = "Hello world. How are you?"
    assert c.capitalize_sentences(text) == expected
