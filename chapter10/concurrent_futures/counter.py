from concurrent.futures import (
    ThreadPoolExecutor,
    wait
)


class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count = self.count + 1


def count_up(counter):
    for _ in range(100000):
        counter.increment()


if __name__ == '__main__':
    counter = Counter()
    threads = 2

    # 2つスレッドを用意し、それぞれでcount_upを呼び出す
    with ThreadPoolExecutor() as e:
        futures = [e.submit(count_up, counter) for _ in range(threads)]

        done, not_done = wait(futures)

    # 値の読み取り→インクリメント→結果を値に代入する の処理の途中で
    # スレッドが切り替わってしまい、self.countに2つのスレッドが
    # 同時にアクセス状況が発生するため、200000にはならない
    print(f'{counter.count=:,}')