#Load known words into a set
def load_lexicon(path):
    with open(path, 'r') as f:
        words = set(line.strip().lower() for line in f)
    return words

#Check if word exist within the lexicon
def is_known(word, lexicon):
    return word in lexicon