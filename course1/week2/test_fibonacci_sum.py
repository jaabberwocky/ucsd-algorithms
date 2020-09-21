from fibonacci_sum import improved_fibo_sum  # noqa


def test1():
    assert improved_fibo_sum(3) == 4
    assert improved_fibo_sum(100) == 5
    assert improved_fibo_sum(1500) == 0
