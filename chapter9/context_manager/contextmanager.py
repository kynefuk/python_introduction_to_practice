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


if __name__ == '__main__':
    with point(hoge='fuga') as f:
        print('本処理')
        print(f)