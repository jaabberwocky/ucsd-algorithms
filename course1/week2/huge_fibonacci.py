def get_mod_from_fibo(n, m):
    pisano = PisanoPeriod(m)
    num = n % pisano.get_period_length()
    return pisano.period[num]


class PisanoPeriod:
    def __init__(self, m):
        self.m = m
        self._derive_period()

    def _derive_period(self):
        fib_nums = []
        period = []

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
        return len(self.period)


if __name__ == "__main__":
    inputs = [int(x) for x in input().split()]
    n, m = inputs[0], inputs[1]
    print(get_mod_from_fibo(n, m))
