import string

def remove_punctuation(text):
    # Create a translation table that removes punctuation
    return text.translate(str.maketrans('', '', string.punctuation))

def count_vowels(text):
    return sum(1 for char in text.lower() if char in 'aeiou')

import re

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
