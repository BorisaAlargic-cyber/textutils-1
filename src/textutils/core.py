import string

def remove_punctuation(text):
    # Create a translation table that removes punctuation
    return text.translate(str.maketrans('', '', string.punctuation))
