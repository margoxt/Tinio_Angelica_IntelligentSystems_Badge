import re

#Extract Tokens
def tokenizer(text):
        tokens = re.findall(r'\\b\\w+\\b', text)

        return tokens

#Convert tokens into lowercase
def normalize(tokens):
        return[t.lower() for t in tokens]