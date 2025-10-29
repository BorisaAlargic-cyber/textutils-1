from textutils.core import (
    is_palindrome,
    word_count,
    average_word_length,
    reverse_words,
    find_unique_words
)

def test_text_processing_pipeline():
    """
    End-to-end integration test for all text processing functions.
    """

    text = "Hello world Hello"

    # Step 1: Reverse words
    reversed_text = reverse_words(text)  # Expect: "Hello world Hello" -> "Hello world Hello"
    assert reversed_text == "Hello world Hello"

    # Step 2: Average word length
    avg_len = average_word_length(reversed_text)  # (5+5+5)/3 = 5.0
    assert avg_len == 5.0

    # Step 3: Word count (case-insensitive)
    counts = word_count(reversed_text)  # {"hello": 2, "world": 1}
    assert counts == {"hello": 2, "world": 1}

    # Step 4: Unique words (case-insensitive)
    uniques = find_unique_words(reversed_text)  # {"hello", "world"}
    assert uniques == {"hello", "world"}

    # Step 5: Palindrome check
    assert is_palindrome("madam") is True
    assert is_palindrome("world") is False
    assert is_palindrome("racecar") is True

    # Step 6: Combined behavior check
    combined_text = "Madam racecar world"
    rev_combined = reverse_words(combined_text)
    counts_combined = word_count(rev_combined)
    assert counts_combined == {"madam": 1, "racecar": 1, "world": 1}
