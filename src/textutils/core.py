import string
import re

def remove_punctuation(text):
    # Create a translation table that removes punctuation
    return text.translate(str.maketrans('', '', string.punctuation))

def count_vowels(text):
    return sum(1 for char in text.lower() if char in 'aeiou')



def capitalize_sentences(text: str) -> str:
    # Split text into parts: sentences + delimiters
    parts = re.split(r'([.!?])', text)
    
    result = []
    for i in range(0, len(parts) - 1, 2):
        sentence = parts[i].strip()
        delimiter = parts[i + 1]
        
        if sentence:
            # Capitalize first letter and add punctuation back
            sentence = sentence[0].upper() + sentence[1:]
            result.append(sentence + delimiter)
    
    # Handle any trailing text or spaces
    return " ".join(s.strip() for s in result)

#word length function

def word_lengths(text: str) -> dict[str, int]:
    """
    Return a dictionary where each word in the text maps to its length.
    Punctuation is ignored and words are treated case-insensitively.

    Example:
        >>> word_lengths("Hello world!")
        {'hello': 5, 'world': 5}
    """
    punctuation = '.,!?;:"()[]{}<>-—\''
    cleaned = text.lower()
    for mark in punctuation:
        cleaned = cleaned.replace(mark, " ")

    words = cleaned.split()

    return {word: len(word) for word in words}

def is_anagram(a: str, b: str) -> bool:
    """
    Checks if two strings are anagrams (case-insensitive, ignores spaces and punctuation).
    """
    import re
    cleaned_a = sorted(re.findall(r"[a-z0-9]", a.lower()))
    cleaned_b = sorted(re.findall(r"[a-z0-9]", b.lower()))
    return cleaned_a == cleaned_b


def is_palindrome(text):
    return text == text[::-1]


def word_count(text):
    text = text.lower()
    words = text.split()
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts

def average_word_length(text: str) -> float:
    words = text.split()
    
    if not words:
        return 0.0
 
    total_length = sum(len(word) for word in words)
    
    return total_length / len(words)

def reverse_words(text):
    return ' '.join(text.split()[::-1])

def find_unique_words(text):

    text = text.lower()
    
    punctuation = '.,!?;:"()[]{}<>-—\''
    for mark in punctuation:
        text = text.replace(mark, ' ')
    
    words = text.split()
    
    unique_words = set(words)
    
    return unique_words