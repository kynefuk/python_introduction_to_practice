from concurrent.futures import (
    ThreadPoolExecutor,
    Future
)


def func():
    return 1


if __name__ == '__main__':
    # 非同期に行いたい処理をsubmitに渡すと、
    # その処理の実行がスケジューリングされて
    # Futureクラスのインスタンスが返される。
    # ThreadPoolExecutorはスレッドベースの非同期実行
    future = ThreadPoolExecutor().submit(func)
    print(isinstance(future, Future))

    # futureはスケジューリングされた呼び出し可能オブジェクトを
    # カプセル化したもので、実行が先送りされている事を表現している。
    # スケジューリングはconcurrent.futuresモジュールが行う。

    # 非同期で実行した処理の戻り値を取得
    print(future.result())

    # 現在の状態を確認する
    print(future.done())
    print(future.running())
    print(future.cancelled())
