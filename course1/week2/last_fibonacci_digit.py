def get_last_fibonacci_digit(n):
    """
    Get last digit of the n-th Fibonacci number. Exploits the observation that the
    last digit is the sum of the preceding two digits.

    Args:
        n (int): n-th Fibonacci number

    Returns:
        int: Last digit of n-th Fibonacci number
    """
    sequence = []
    add_first_two_fib(sequence)

    for i in range(2, n+1):
        last_digit = sequence[i-2] + sequence[i-1]
        sequence.append(last_digit % 10)
    return sequence[-1]


def add_first_two_fib(sequence):
    """
    Adds the first two Fibonacci numbers (0 and 1) to the sequence of numbers.

    Args:
        sequence (list): List of Fibonacci numbers
    """
    sequence.append(0)
    sequence.append(1)


if __name__ == "__main__":
    n = int(input())
    print(get_last_fibonacci_digit(n))
