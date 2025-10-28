import textutils.core as c

def test_remove_punctuation_basic():
    text = "Hello, world!"
    assert c.remove_punctuation(text) == "Hello world"
