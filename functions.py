def fib(n):    # write Fibonacci series up to n

    a = 0
    b = 1
    while a < n:
        print a,
        a = b
        b = a + b
        # a, b = b, a+b


fib(2000)
