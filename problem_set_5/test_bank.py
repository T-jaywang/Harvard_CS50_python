from bank_ import value

def test_startwith_hello():
    assert value("hello, my name is jay.") == "$0"

def test_startwith_h_letter():
    assert value("how is going?") == "$20"

def test_violate():
    assert value("good morning!") == "$100"