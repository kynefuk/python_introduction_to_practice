from concurrent.futures import (
    ThreadPoolExecutor,
    as_completed
)
from download import urls, elapsed_time, download


@elapsed_time
def get_multi_thread():
    # max_workersのデフォルトはコア数×5
    with ThreadPoolExecutor(max_workers=3) as executor:
        # download()に渡す値を第二引数に指定
        futures = [executor.submit(download, url) for url in urls]


        # as_completed()は処理が完了したものから順に返す
        for future in as_completed(futures):
            # 完了したものからresultが表示される
            print(future.result())


if __name__ == '__main__':

    get_multi_thread()