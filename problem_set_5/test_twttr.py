from problem_set_5.twttr import shorten

def test_lowercase():
    assert shorten("twitter") == "twttr"

def test_uppercase():
    assert shorten("TWITTER") == "TWTTR"

def test_mixed_case():
    assert shorten("TwItTeR") == "TwtTR"

def test_with_numbers():
    assert shorten("CS50") == "CS50"  

def test_with_punctuation():
    assert shorten("email!") == "ml!"

def test_only_vowels():
    assert shorten("aeiouAEIOU") == ""