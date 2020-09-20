def naive_gcd(a, b):
    """Naive implementation in O(n) time.

    Args:
        a (int): First integer
        b (int): Second integer

    Returns:
        int: Greatest common divisor
    """
    for i in range(1, a+b):
        if a % i == 0 and b % i == 0:
            greatest = i
    return greatest


def improved_gcd(a, b):
    """Euclidean's algorithm for faster performance O(log n) time.

    Args:
        a (int): First integer
        b (int): Second integer

    Returns:
        int: Greatest common divisor
    """
    if b == 0:
        return a
    else:
        a_prime = a % b
        return improved_gcd(b, a_prime)
