import textutils.core as c

def test_text_processing_pipeline():
    """
    Integration test combining multiple functions:
    - reverse_words
    - average_word_length
    - word_count
    - unique_words
    - is_palindrome
    """
    text = "Hello world Hello"

    # Step 1: Reverse words
    reversed_text = c.reverse_words(text)  # "Hello world Hello" -> "Hello world Hello"

    # Step 2: Compute average word length
    avg_len = c.average_word_length(reversed_text)  # (5+5+5)/3 = 5.0

    # Step 3: Count words
    counts = c.word_count(reversed_text)  # {"Hello": 2, "world": 1}

    # Step 4: Get unique words
    uniques = c.find_unique_words(reversed_text)  # {"Hello", "world"}

    # Step 5: Check palindrome behavior
    palindrome_text = "madam"
    not_palindrome_text = "world"
    is_pal = c.is_palindrome(palindrome_text)
    is_not_pal = c.is_palindrome(not_palindrome_text)

    # Assertions
    assert reversed_text == "Hello world Hello"
    assert avg_len == 5.0
    assert counts == {"Hello": 2, "world": 1}
    assert uniques == {"Hello", "world"}
    assert is_pal is True
