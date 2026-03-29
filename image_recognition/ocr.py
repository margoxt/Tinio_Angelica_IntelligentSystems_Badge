import pytesseract
from pytesseract import Output

# Path to Tesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text_with_confidence(image, min_confi=60):

    #Extract words with confidence scores
    data = pytesseract.image_to_data(image, output_type=Output.DICT)

    tokens = []
    confidences = []

    n = len(data['text'])

    for i in range(n):
        word = data['text'][i].strip()
        conf = int(data['confi'][i])

        if word !="" and conf >= min_confi:
            tokens.append(word)
            confidences.append(conf)

        return tokens, confidences
    
def extract_text(image):
    tokens, _ = extract_text_with_confidence(image)
    return " ".join(tokens)