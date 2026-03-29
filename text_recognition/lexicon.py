# Load known words into a SET (fast lookup)
def load_lexicon(path):
    with open(path, 'r') as f:
        words = set(line.strip().lower() for line in f)
    return words


# Check if a word exists in lexicon
def is_known(word, lexicon):
    return word in lexicon