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


def get_last_digit(num):
    """
    Get last digit of a number.

    Args:
        num (int): Number

    Returns:
        int: Last digit
    """
    return num % 10


def get_last_fibonacci_digit(n):
    """
    Get last digit of the n-th Fibonacci number.

    Args:
        n (int): n-th Fibonacci number

    Returns:
        int: Last digit of n-th Fibonacci number
    """
    fib = improved_fib(n)
    return get_last_digit(fib)


if __name__ == "__main__":
    n = int(input())
    print(get_last_fibonacci_digit(n))
