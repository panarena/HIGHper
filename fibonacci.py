from itertools import islice


def fibonacci():
    i, j = 0, 1
    while True:
        yield j
        i, j = j, i + j


def fibonacci_naive():
    i, j = 0, 1
    count = 0
    while j <= 5000:
        if j % 2:
            count += 1
        i, j = j, i + j
    return count


def fibonacci_generator(parMax : int):
    count = 0
    for f in fibonacci():
        print(f)
        if f > parMax:
            break
        if (f % 2):
            count += 1
    return count


def fibonacci_succinct(parMax : int):
    is_odd = lambda x: x % 2
    # islice takes the first parMax Fibonacci numbers and not all Fibonacci number smaller parMax
    first_parMax = islice(fibonacci(), 0, parMax)
    return sum(1 for f in first_parMax if is_odd(f))

print(fibonacci_generator(5000))
print(fibonacci_succinct(19))