# 引数zを受け取る
def deco3(z):
    print('deco3 exec')

    def _deco3(f):
        print('_deco3 exec')

        def wrapper(*args, **kwargs):
            print('before exec', z)
            f(*args, **kwargs)
            print('after exec', z)
        return wrapper
    return _deco3

# deco3(z=3)の戻り値がデコレータの実体
# つまりsample = deco3(z=3)(func)と同等
# 関数の定義時にdeco3(z=3)が実行され、その結果として
# _deco3()が返される。
# _deco3()が関数sampleを引数として呼び出され、
# その結果wrapper()が元の関数に置き換えられる。
@deco3(z=3)
def sample(x, y):
    print('exec')
    print(x, y)


if __name__ == '__main__':
    sample(1, 2)