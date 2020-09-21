def get_mod_from_fibo(n, m):
    """
    Returns the value of the n-th Fibonacci number mod by m.

    Args:
        n (int): n-th Fibonacci number
        m (int): mod

    Returns:
        int: Value of n-th Fibonacci number mod by m
    """
    pisano = PisanoPeriod(m)
    num = n % pisano.get_period_length()
    return pisano.period[num]


class PisanoPeriod:
    """
    Class for calculating a pisano period.
    """

    def __init__(self, m):
        """
        Initialises period to hold m and the calculated period.

        Args:
            m (int): mod factor
        """
        self.m = m
        self._derive_period()

    def _derive_period(self):
        """
        Derives period for given m.
        """
        fib_nums = []
        period = []

        # initialise arrays to cover first two iterations
        fib_nums.append(0)
        fib_nums.append(1)
        period.append(0)
        period.append(1)

        ctr = 2
        while True:
            if period[ctr - 2] == 0 and period[ctr - 1] == 1 and ctr != 2:
                break
            fib = fib_nums[ctr - 2] + fib_nums[ctr - 1]
            fib_nums.append(fib)
            period.append(fib % self.m)
            ctr += 1
        self.period = period[:-2]

    def get_period_length(self):
        """
        Returns length of calculated period.

        Returns:
            int: Length of calculated period
        """
        return len(self.period)


if __name__ == "__main__":
    inputs = [int(x) for x in input().split()]
    n, m = inputs[0], inputs[1]
    print(get_mod_from_fibo(n, m))
