import sys
sys.set_int_max_str_digits(0)


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib_gen = fibonacci()

positions = [5, 200, 1000, 100000]
results = {}

for i in range(1, max(positions) + 1):
    fib_number = next(fib_gen)
    if i in positions:
        results[i] = fib_number

for pos in positions:
    print(f"The {pos}th Fibonacci number is: {results[pos]}")
