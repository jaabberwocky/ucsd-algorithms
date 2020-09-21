class LastDigitFibo:
    def __init__(self):
        self.init_sequence()

    def init_sequence(self):
        last_digits = []
        last_digits.append(0)
        last_digits.append(1)

        for i in range(2, 60):
            last_digits.append(improved_fib(i) % 10)
        self.sequence = last_digits

    def get_sequence(self):
        return self.sequence

    def get_last_digit_of_sum(self, n):
        return self.sequence[n % 60]


def improved_fib(n):
    """Improved implementation in O(n) time.

    Args:
        n (int): Number to generate a Fibonacci number for.

    Returns:
        int: Fibonacci number for sequence n.
    """
    sequence = []

    for i in range(n+1):
        if i in [0, 1]:
            sequence.append(i)
        else:
            sequence.append(sequence[i - 1] + sequence[i - 2])

    return sequence[-1]


if __name__ == "__main__":
    n = int(input())
    L = LastDigitFibo()
    print(L.get_last_digit_of_sum(n))
