import textutils.core as c

def test_textutils_functions():
    # --- Test 1: remove_punctuation ---
    text = "Hello, world!!! How's it going?"
    assert c.remove_punctuation(text) == "Hello world Hows it going"

    # --- Test 2: count_vowels ---
    assert c.count_vowels("Hello World") == 3  # e, o, o

    # --- Test 3: capitalize_sentences ---
    text = "hello world. this is a test! is it working?"
    expected = "Hello world. This is a test! Is it working?"
    assert c.capitalize_sentences(text) == expected

    # --- Test 4: word_lengths ---
    text = "Hello world! Python is fun."
    expected = {"hello": 5, "world": 5, "python": 6, "is": 2, "fun": 3}
    assert c.word_lengths(text) == expected

    # --- Test 5: is_anagram ---
    assert c.is_anagram("Listen", "Silent") is True
    assert c.is_anagram("Astronomer", "Moon starer") is True
    assert c.is_anagram("Hello", "Olelh") is True
    assert c.is_anagram("Hello", "World") is False




def test_textutils_functions_1():
    # --- Test 1: remove_punctuation ---
    text = "Hello, world!!! How's it going?"
    assert c.remove_punctuation(text) == "Hello world Hows it going"

    # --- Test 2: count_vowels ---
    assert c.count_vowels("Hello World") == 3  # e, o, o

    # --- Test 3: capitalize_sentences ---
    text = "hello world. this is a test! is it working?"
    expected = "Hello world. This is a test! Is it working?"
    assert c.capitalize_sentences(text) == expected

    # --- Test 4: word_lengths ---
    text = "Hello world! Python is fun."
    expected = {"hello": 5, "world": 5, "python": 6, "is": 2, "fun": 3}
    assert c.word_lengths(text) == expected

    # --- Test 5: is_anagram ---
    assert c.is_anagram("Listen", "Silent") is True
    assert c.is_anagram("Astronomer", "Moon starer") is True
    assert c.is_anagram("Hello", "Olelh") is True
    assert c.is_anagram("Hello", "World") is False