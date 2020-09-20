def naive_fib(n):
    if n <= 1:
        return n
    else:
        return naive_fib(n-1) + naive_fib(n-2)
