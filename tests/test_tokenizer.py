from text_recognition.tokenizer import tokenize

def test_basic_tokenization():
    text = "Hellow world 2026-03-29"
    tokens = tokenize(text)

    assert "Hello" in tokens
    assert "world" in tokens
    assert "2026-03-29" in tokens

def test_hyphenated():
    text = "amazing-world-of-gumball"
    tokens = tokenize(text)

    assert "amazing-world-of-gumball" in tokens