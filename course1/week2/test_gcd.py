from gcd import naive_gcd, improved_gcd  # noqa


def test_naive_gcd():
    f = naive_gcd
    assert f(10, 4) == 2
    assert f(25, 5) == 5
    assert f(357, 234) == 3


def test_improved_gcd():
    f = improved_gcd
    assert f(10, 4) == 2
    assert f(25, 5) == 5
    assert f(357, 234) == 3
