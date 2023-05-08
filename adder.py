def add(x: int, y: int) -> int:
    """
    Computes the sum of x and y
    """
    return x + y


def test_add():
    x = 1
    y = 1
    assert add(x, y) == 2
