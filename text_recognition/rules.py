import re

# RULE 1: Check if number
def is_number(token):
    return bool(re.match(r'^\d+(\.\d+)?$', token))


# RULE 2: Proper noun (use original token)
def is_proper_noun(token):
    return bool(re.match(r'^[A-Z][a-z]+$', token))


# RULE 3: Date pattern (simple YYYY-MM-DD)
def is_date(token):
    return bool(re.match(r'^\d{4}-\d{2}-\d{2}$', token))


# RULE 4: Hyphenated word
def is_hyphenated(token, lexicon):
    if '-' in token:
        parts = token.split('-')
        return all(p in lexicon for p in parts)
    return False


# RULE 5: Too long 
def is_too_long(token):
    return len(token) > 30