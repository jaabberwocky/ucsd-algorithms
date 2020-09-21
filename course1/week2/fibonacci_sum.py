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
    last_fib = 1
    second_last_fib = 0

    for _ in range(2, n+1):
        fib = last_fib + second_last_fib
        second_last_fib = last_fib
        last_fib = fib
    return fib


if __name__ == "__main__":
    n = int(input())
    print(improved_fibo_sum(n))
