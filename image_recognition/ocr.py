import pytesseract
from pytesseract import Output

# Set path to Tesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def extract_text_with_confidence(image, min_conf=60):

    data = pytesseract.image_to_data(image, output_type=Output.DICT)

    tokens = []
    confidences = []

    n = len(data['text'])

    for i in range(n):
        word = data['text'][i].strip()
        conf = int(data['conf'][i])

        # Only keep good words
        if word != "" and conf >= min_conf:
            tokens.append(word)
            confidences.append(conf)

    return tokens, confidences

def extract_text(image):
    tokens, _ = extract_text_with_confidence(image)
    return " ".join(tokens)