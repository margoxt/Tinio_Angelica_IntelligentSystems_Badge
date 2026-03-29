from text_recognition.rules import *

def classify_tokens(tokens, original_token, lexicon):

    #Storage of Results
    results = []

    for i, token in enumerate(tokens):
        original = original_token[i]

        classification = []
        rules_fired = []

        # Date
        if is_date(original):
            classification.append("DATE")
            rules_fired.append("is_date")

        # Number
        if is_number(token):
             classification.append("NUMBER")
             rules_fired.append("is_number")

        # Proper Noun
        if is_proper_noun(original):
             classification.append("PROPER_NOUN")
             rules_fired.append("is_proper_noun")

        # Known Word
        if token in lexicon:
             classification.append("KNOWN_WORD")
             rules_fired.append("lexicon_lookup")

        # Hyphenated word
        if is_hyphenated(token, lexicon):
             classification.append("HYPHENATED_KNOWN")
             rules_fired.append("is_hyphenated")

        # Overly-long
        if is_too_long(token):
             classification.append("INVALID_LONG")
             rules_fired.append("too_long")

        results.append({
             "token": original,
             "normalized": token,
             "classification": classification,
             "rules_fired": rules_fired
        })

    return results
