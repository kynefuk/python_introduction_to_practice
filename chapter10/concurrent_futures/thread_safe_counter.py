import threading
from concurrent.futures import (
    ThreadPoolExecutor,
    wait
)

from counter import count_up


class ThreadSafeCounter:
    lock = threading.Lock()

    def __init__(self):
        self.count = 0

    def increment(self):

        with self.lock:
            # 排他制御したい処理をブロック内に書く
            # ロックを獲得したスレッドがこの処理を行い,
            # 処理が終わったら速やかにロックを開放する。
            # ロックの開放漏れを防ぐためにwith文を使う
            self.count = self.count + 1


if __name__ == '__main__':
    counter = ThreadSafeCounter()
    threads = 2

    with ThreadPoolExecutor() as e:
        futures = [e.submit(count_up, counter) for _ in range(threads)]
        done, not_done = wait(futures)

    print(f'{counter.count=:,}')
