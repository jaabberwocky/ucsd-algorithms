def naive_implementation(a):
    """
    Naive implementation using brute force.

    Args:
        a (list): List containing non-negative integers.

    Returns:
        int: Maximum product
    """
    max = 0
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            prod = a[i] * a[j]
            if prod > max:
                max = prod
    return max


def fast_implementation(a):
    """
    Fast implementation using O(n) time.

    Args:
        a (list): List containing non-negative integers.

    Returns:
        int: Maximum product
    """
    largest = 0
    second_largest = 0
    largest_pos = 0
    second_largest_pos = 0

    for ind, val in enumerate(a):
        if val > largest:
            largest = val
            largest_pos = ind

    for ind, val in enumerate(a):
        if ind == largest_pos:
            next
        elif val > second_largest:
            second_largest = val
            second_largest_pos = ind

    return a[largest_pos] * a[second_largest_pos]


if __name__ == "__main__":
    n = int(input())
    a = [int(x) for x in input().split()]
    print(fast_implementation(a))
