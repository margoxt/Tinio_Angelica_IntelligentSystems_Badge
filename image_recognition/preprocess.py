import cv2

def preprocess_image(path):
    img = cv2.imread(path)

    if img is None:
        raise FileNotFoundError(f"Image not found at path: {path}")

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    _, simple_thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

    return simple_thresh