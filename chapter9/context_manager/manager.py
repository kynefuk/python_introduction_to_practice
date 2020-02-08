class ContextManager:

    # withブロックに入る際に実行される前処理を実装
    def __enter__(self):
        print('__enter__ was called')

        # __enter__()の戻り値にすることで
        # asキーワードで受け取れる
        return (1, 2, 3, 4, 5)

    # withブロックを抜ける際に実行される後処理を実装
    # 例外が送出された場合は、引数でその情報を受け取れる
    def __exit__(self, exc_type, exc_value, traceback):
        print('__exit__ was called')
        print(f'{exc_type=}')
        print(f'{exc_value=}')
        print(f'{traceback=}')


if __name__ == '__main__':
    with ContextManager() as f:
        print('inside the block')
        # __enter__()の戻り値がasに入る
        print(f)

# __enter__の処理→withブロック内の処理→__exit__の処理の順番で処理が行われる。
