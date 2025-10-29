import textutils.core as c

def test_word_count_basic():
    text = "Cat dog cat"
    assert c.word_count(text) == {"cat": 2, "dog": 1}
