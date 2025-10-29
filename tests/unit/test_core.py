#unique_words function tests
import textutils.core as c
def test_find_unique_words_basic():
    """Check basic functionality with repeated words."""
    text = "Hello hello world"
    result = c.find_unique_words(text)
    assert result == {"hello", "world"}


def test_find_unique_words_with_punctuation():
    """Ensure punctuation does not affect unique words."""
    text = "Red, blue! Red... blue? Green."
    result = c.find_unique_words(text)
    assert result == {"red", "blue", "green"}