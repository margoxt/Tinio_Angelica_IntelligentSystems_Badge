import re

# This function extracts words, numbers, and hyphenated words
def tokenize(text):
    tokens = re.findall(r'\b\w+(?:-\w+)*\b', text)

    return tokens

# Convert all tokens to lowercase
def normalize(tokens):
    return [t.lower() for t in tokens]