from fibonacci import naive_fib


def test_fib_small():
    assert naive_fib(3) == 2
    assert naive_fib(2) == 1
    assert naive_fib(1) == 1
    assert naive_fib(0) == 0
