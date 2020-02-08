from contextlib import contextmanager
@contextmanager
def point(**kwargs):
    print('__enter__ was called')
    value = kwargs

    try:
        # yield式より上に前処理を書く
        print(f'前処理です')

        # yieldで返される値がasキーワードに入る
        yield value

        # yield式より下に後処理を書く
        print(f'後処理です')
    except Exception as e:
        print(e)
        raise
    finally:
        print('__exit__ was called')


if __name__ == '__main__':
    with point(hoge='fuga') as f:
        print('本処理')
        print(f)