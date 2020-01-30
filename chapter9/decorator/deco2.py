def deco2(f):
    # デコレートする関数の引数を受け取るために
    # wrapper関数が引数を受け取れるようにする
    def wrapper(*args, **kwargs):
        print('before exec')
        # 引数を渡して元の関数を実行
        f(*args, **kwargs)
        print('after exec')

    return wrapper


@deco2
def sample(x, y):
    print('exec')
    print(x, y)


if __name__ == '__main__':
    sample(1, 2)