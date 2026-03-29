## Text Mode
Tokenization -> Normalization -> Lexicon Lookup & Rule Classification -> Output Json

## Image Mode
Image-Preprocessing -> OCR -> OCR Post-processing -> Lexicon Lookup & Rule Classification -> Output Json

-----------------------------

## Notes:
* Tokenization: Regex-based
* Lexicon: Implemented as Python set
* Rules: date, number, proper noun, hyphenated words, too-long tokens
* OCR: uses pytesseract with optional confidence filtering
* Preprocessing: grayscale & thresholding

-----------------------------