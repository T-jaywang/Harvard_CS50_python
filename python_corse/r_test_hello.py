from p_hello import hello


def test_default():
    assert hello() == "hello, world"

def test_arguement():
    for name in ["Hermione","Harry","Ron"]:
        assert hello(name) == f"hello, {name}"
