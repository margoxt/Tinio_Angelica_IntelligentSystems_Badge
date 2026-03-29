import argparse
import json

from text_recognition.tokenizer import tokenize, normalize
from text_recognition.lexicon import load_lexicon
from text_recognition.engine import classify_tokens

from image_recognition.preprocess import preprocess_image
from image_recognition.ocr import extract_text_with_confidence
from image_recognition.postprocess import process_ocr_tokens

def run_text_mode(text, lexicon):
    tokens = tokenize(text)
    normalized = normalize(tokens)

    results = classify_tokens(normalized, tokens, lexicon)

    return {"mode": "text", "results": results}


def run_image_mode(image_path, lexicon):
    processed_img = preprocess_image(image_path)

    tokens, confidences = extract_text_with_confidence(processed_img)

    tokens, normalized = process_ocr_tokens(tokens)

    results = classify_tokens(normalized, tokens, lexicon)

    # Attach confidence to output
    for i in range(len(results)):
        results[i]["confidence"] = confidences[i]

    return {"mode": "image", "results": results}


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--lexicon", required=True)
    parser.add_argument("--text")
    parser.add_argument("--image")

    args = parser.parse_args()

    lexicon = load_lexicon(args.lexicon)

    if args.text:
        output = run_text_mode(args.text, lexicon)

    elif args.image:
        output = run_image_mode(args.image, lexicon)

    else:
        print("Provide --text or --image")
        return

    print(json.dumps(output, indent=4))


if __name__ == "__main__":
    main()
    