from hello import hello


def test_default():
    assert hello() == "hello, world"

def test_arguement():
    assert hello("Jay") == "hello, Jay"
