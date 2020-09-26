from algo_course1.week2.fibonacci_sum_squares import LastDigitFibo


def test1():
    L = LastDigitFibo()
    assert L.get_last_digit_of_sum_of_squares(7) == 3
    assert L.get_last_digit_of_sum_of_squares(73) == 1
    assert L.get_last_digit_of_sum_of_squares(1234567890) == 0