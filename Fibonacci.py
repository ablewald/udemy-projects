def fibo(n):
    """
    :param n:
    :return yield first n elements of the fibonacci sequence :
    """

    a = 1
    b = 1
    for i in range(n):
        yield a
        a, b = b, a+b


for i in fibo(1000):
    print (i)

