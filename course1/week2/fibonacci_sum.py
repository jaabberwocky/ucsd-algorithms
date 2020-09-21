def naive_fibo_sum(n):
    seq = []
    seq.append(0)
    seq.append(1)
    sum = 1

    for i in range(2, n+1):
        fib = seq[i - 2] + seq[i - 1]
        sum += fib
        seq.append(fib)

    return sum % 10


def improved_fibo_sum(n):
    sum = improved_fib(n + 2) - 1
    return sum % 10


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
    print(improved_fibo_sum(n))
