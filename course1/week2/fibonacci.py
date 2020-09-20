def naive_fib(n):
    """Naive recursive implementation of Fibonacci generator.

    Args:
        n (int): Number to generate a Fibonacci number for

    Returns:
        int: Fibonacci number for sequence n.
    """
    if n <= 1:
        return n
    else:
        return naive_fib(n-1) + naive_fib(n-2)


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
