import os
import sys
from concurrent.futures import (
    ProcessPoolExecutor,
    as_completed
)

from fib import elapsed_time, fibonacci


@elapsed_time
def get_multi_process(nums):
    with ProcessPoolExecutor() as e:
        futures = [e.submit(fibonacci, num) for num in nums]

        # as_completed()は処理が完了したものから順に返す
        for future in as_completed(futures):
            print(future.result())


def main():
    n = int(sys.argv[1])
    nums = [n] * os.cpu_count()
    get_multi_process(nums)


if __name__ == '__main__':
    main()
