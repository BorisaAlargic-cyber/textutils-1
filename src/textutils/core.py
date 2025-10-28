def average_word_length(text: str) -> float:
    words = text.split()
    
    if not words:
        return 0.0
 
    total_length = sum(len(word) for word in words)
    
    return total_length / len(words)