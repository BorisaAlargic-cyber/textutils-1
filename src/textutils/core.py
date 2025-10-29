def find_unique_words(text):
    """
    Returns a set of unique words in the given text,
    without using the 're' module.
    """
    # Convert to lowercase for consistency
    text = text.lower()
    
    # Replace common punctuation with spaces
    punctuation = '.,!?;:"()[]{}<>-—\''
    for mark in punctuation:
        text = text.replace(mark, ' ')
    
    # Split text into words based on whitespace
    words = text.split()
    
    # Create a set of unique words
    unique_words = set(words)
    
    return unique_word