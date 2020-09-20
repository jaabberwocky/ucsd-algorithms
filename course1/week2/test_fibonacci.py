from fibonacci import naive_fib, improved_fib  # noqa


def test_naive_fib_small():
    assert naive_fib(3) == 2
    assert naive_fib(2) == 1
    assert naive_fib(1) == 1
    assert naive_fib(0) == 0


def test_naive_fib_large():
    # assert naive_fib(50) == 12586269025 # will not run in time
    assert naive_fib(20) == 6765
    assert naive_fib(10) == 55


def test_improved_fib_small():
    assert improved_fib(3) == 2
    assert improved_fib(2) == 1
    assert improved_fib(1) == 1
    assert improved_fib(0) == 0


def test_improved_fib_large():
    assert improved_fib(50) == 12586269025
    assert improved_fib(20) == 6765
    assert improved_fib(10) == 55
