import re

def capitalize_sentences(text: str) -> str:
    """
    Capitalizes the first letter of each sentence in the input text.
    Sentences are assumed to end with '.', '!', or '?'.
    """
    if not text:
        return ""

    # Split text into sentences while keeping punctuation
    sentences = re.split(r'([.!?])', text)
    
    # Capitalize first character of each sentence (strip leading spaces)
    capitalized_sentences = []
    for i in range(0, len(sentences)-1, 2):
        sentence = sentences[i].strip()
        punctuation = sentences[i+1]
        if sentence:
            sentence = sentence[0].upper() + sentence[1:]
        capitalized_sentences.append(sentence + punctuation)
    
    # Handle any leftover text without punctuation
    if len(sentences) % 2 != 0:
        leftover = sentences[-1].strip()
        if leftover:
            leftover = leftover[0].upper() + leftover[1:]
            capitalized_sentences.append(leftover)
    
    # Join sentences with a space
    return " ".join(capitalized_sentences)

def camel_to_snake(text): 
    # Insert underscore between a lowercase/number and uppercase letter
    text = re.sub(r'(?<=[a-z0-9])([A-Z])', r'_\1', text)
    # Convert the whole string to lowercase
    return text.lower()
