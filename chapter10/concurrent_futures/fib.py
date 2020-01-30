import os
import time
import sys


def elapsed_time(f):
    def wrapper(*args, **kwargs):
        start = time.time()
        v = f(*args, **kwargs)
        print(f'{f.__name__}: {time.time() - start}')
        return v
    return wrapper


def fibonacci(n):
    a, b = 0, 1

    for _ in range(n):
        a, b = b, b + a
    else:
        return a


@elapsed_time
def get_sequential(nums):
    for num in nums:
        print(fibonacci(num))


def main():
    n = int(sys.argv[1])
    nums = [n] * os.cpu_count()
    get_sequential(nums)


if __name__ == '__main__':
    main()