from text_recognition.rules import is_number, is_date

def test_number():
    assert is_number("123")
    assert is_number("3.14")

def test_date():
    assert is_date("2026-01-06")