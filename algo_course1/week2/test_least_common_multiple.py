from least_common_multiple import least_common_multiple  # noqa


def test_lcm():
    assert least_common_multiple(6, 8) == 24
    assert least_common_multiple(761457, 614573) == 467970912861
