from algo_course1.week2.huge_fibonacci import get_mod_from_fibo  # noqa


def test1():
    assert get_mod_from_fibo(10, 2) == 1
    assert get_mod_from_fibo(10, 3) == 1
    assert get_mod_from_fibo(15, 2) == 0
    assert get_mod_from_fibo(3, 3) == 2


def test2():
    assert get_mod_from_fibo(239, 1000) == 161
    assert get_mod_from_fibo(2816213588, 239) == 151
    assert get_mod_from_fibo(1111, 6) == 1
