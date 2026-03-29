import cv2

def preprocess_image(path):
    img = cv2.imread(path)

    if img is None:
        raise FileNotFoundError(f"Image not found at path: {path}")
    
    gray = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

    _, simple_threshold = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

    return simple_threshold