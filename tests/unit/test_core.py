import textutils.core as c

def test_average_word_length_basic():
    text = "Hello world! This is a test."
    assert c.average_word_length(text) == 23 / 6