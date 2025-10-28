import re

def camel_to_snake(text): 
    # Insert underscore between a lowercase/number and uppercase letter
    text = re.sub(r'(?<=[a-z0-9])([A-Z])', r'_\1', text)
    # Convert the whole string to lowercase
    return text.lower()
