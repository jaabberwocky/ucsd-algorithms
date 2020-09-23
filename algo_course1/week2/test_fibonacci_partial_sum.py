from algo_course1.week2.fibonacci_partial_sum import LastDigitFibo


def test1():
    L = LastDigitFibo()
    assert L.get_last_digit_of_partial_sum(3, 7) == 1
    assert L.get_last_digit_of_partial_sum(10, 10) == 5
    assert L.get_last_digit_of_partial_sum(10, 200) == 2
    assert L.get_last_digit_of_partial_sum(1, 1) == 1
