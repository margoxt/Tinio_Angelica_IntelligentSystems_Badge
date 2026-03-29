import re

# RULE 1: Proper Noun Check
def is_proper_noun(token):
    return bool(re.match(r'^[A-Z][a-z]+$'), token)

# RULE 2: Number Check
def is_number(token):
    return bool(re.match(r'^\d+$', token))

# RULE 3: Date Pattern
def is_date(token):
    return bool(re.match(r'^\d{4}-\d{2}-\d{2}$', token))

# RULE 4: Hyphenated Word
def is_hyphenated(token, lexicon):
    if '-' in token:
        parts = token.split('-')
        return all(p in lexicon for p in parts)
    return False

# RULE 5: Overly-long Token
def is_too_long(token):
    return len(token) > 30
