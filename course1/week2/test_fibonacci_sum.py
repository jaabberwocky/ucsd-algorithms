from fibonacci_sum import LastDigitFibo  # noqa


def test1():
    L = LastDigitFibo()
    assert L.get_last_digit_of_sum(3) == 4
    assert L.get_last_digit_of_sum(100) == 5
    assert L.get_last_digit_of_sum(0) == 0
    assert L.get_last_digit_of_sum(2) == 2
    assert L.get_last_digit_of_sum(614162383528) == 9
