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

if __name__=="__main__":
    n = int(input())
    a = [int(x) for x in input().split()]
    print(naive_implementation(a))
