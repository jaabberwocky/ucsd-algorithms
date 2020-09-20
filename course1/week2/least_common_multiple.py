def least_common_multiple(a, b):
    """
    Generates the least common multiple which is divisible by both a and b.

    Args:
        a (int): First number
        b (b): Second number

    Returns:
        int: Least common multiple
    """
    for i in range(1, b+1):
        num = a * i
        if num % b == 0:
            return num


if __name__ == "__main__":
    n = [int(x) for x in input().split()]
    a, b = n[0], n[1]
    print(least_common_multiple(a, b))
