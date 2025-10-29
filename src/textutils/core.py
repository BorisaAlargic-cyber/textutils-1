

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