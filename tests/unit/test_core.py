import textutils.core as c

def test_reverse_words():
    text = "Hello World, my name is Jerico Agdan"
    assert c.reverse_words(text)