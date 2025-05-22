from plates import is_valid

def test_is_valid():
    assert is_valid("A") == False
    assert is_valid("AA22A") == False
    assert is_valid("AAA012") == False
    assert is_valid("AA,222") == False 