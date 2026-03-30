## Install Dependencies
pip install pytest
pip install pytesseract pillow opencv-python

-----------------------------

## ✅ Student Checklist

### Core Functionality
- `--text` mode prints structured JSON output with rules fired  
- `--image` mode performs OCR and token classification  
- Lexicon dynamically loaded from `--lexicon` path  

### Rule-Based System
-  Implemented rules:
  - Date detection (`YYYY-MM-DD`)
  - Number detection
  - Proper noun detection
  - Hyphenated word detection
  - Token length validation  
   Each rule documented and explained in README  

### Performance & Analysis
- [x] Complexity review includes:
  - Big-O analysis (time & space)
  - Empirical runtime measurements  
- [x] Observations and trade-offs discussed  

### Testing
-  Unit tests implemented for:
  - Tokenizer
  - Rules
  - OCR post-processing  
-  Tests executed using `pytest`  

### Submission Requirements
- [x] GitHub repository link submitted  
- OneDrive video demo (Teams recording) submitted: https://hauph-my.sharepoint.com/:v:/g/personal/aztinio_student_hau_edu_ph/IQCR_A4pN6BXQKOvg6qMkPHvAf0Mb3F25YTMf0GVwlRUbPo?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=AxbdS3
- https://hauph-my.sharepoint.com/:v:/g/personal/aztinio_student_hau_edu_ph/IQBxofVcUCnkQoouiip6xly8AbPynY5mlqagtJ8uVrCu7Fw?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&email=mlsalenga%40hau.edu.ph&e=RwHKKK

### Documentation
#### Text
python cli.py --lexicon data/lexicon_en.txt --text "<Enter text here>"

#### Image
python cli.py --lexicon data/lexicon_en.txt --image data/sample_images/sample3.jpg

#### Sample Output
#### Image:
![Image Output](imagetest.png)

#### Text:
![Text Output](textpart1.png)
![Text Output](textpart2.png)
![Text Output](testpart3.png)
![Text Output](testpart4.png)

-----------------------------
