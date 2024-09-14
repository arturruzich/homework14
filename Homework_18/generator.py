def numbers_generator(N):
    for num in range(0, N+1, 2):
        yield num

for even in numbers_generator(10):
    print(even)


def fibonacci_generator(N):
    a, b = 0, 1
    while a <= N:
        yield a
        a, b = b, a + b

for fib in fibonacci_generator(10):
    print(fib)