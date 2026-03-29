from text_recognition.tokenizer import normalize

def process_ocr_tokens(tokens):
    normalized = normalize(tokens)
    return tokens, normalized