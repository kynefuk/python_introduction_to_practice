class ContextManager:

    # 前処理を実装
    def __enter__(self):
        print('__enter__ was called')

        # __enter__()の戻り値にすることで
        # asキーワードで受け取れる
        return 1

    # 後処理を実装
    # 例外が送出された場合は、引数でその情報を受け取れる
    def __exit__(self, exc_type, exc_value, traceback):
        print('__exit__ was called')
        print(f'{exc_type=}')
        print(f'{exc_value=}')
        print(f'{traceback=}')


from contextlib import contextmanager
@contextmanager
def point(**kwargs):
    print('__enter__ was called')
    value = kwargs

    try:
        # yield式より上に前処理を書く

        # valueがasキーワードに渡される
        yield value

        # yield式より下に後処理を書く
    except Exception as e:
        print(e)
        raise
    finally:
        print('__exit__ was called')
        print(value)

if __name__ == '__main__':
    with ContextManager() as f:
        print('inside the block')
        # __enter__()の戻り値がasに入る
        print(f)
