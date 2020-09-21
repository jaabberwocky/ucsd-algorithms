from fibonacci_sum import LastDigitFibo  # noqa


def test1():
    L = LastDigitFibo()
    assert L.get_last_digit_of_sum(4) == 3
    assert L.get_last_digit_of_sum(100) == 5
    assert L.get_last_digit_of_sum(1500) == 0
    assert L.get_last_digit_of_sum(0) == 0
