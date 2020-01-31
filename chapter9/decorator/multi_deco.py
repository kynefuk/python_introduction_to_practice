def deco(z):
    def _deco(f):
        def wrapper(*args, **kwargs):
            print('before exec', z)
            f(*args, **kwargs)
            print('after exec', z)
        return wrapper
    return _deco


# deco(z=5)→deco(z=3)の順で実行される
# deco(z=5)によって返されるwrapperが
# deco(z=3)内で更にデコレートされ
# 最終的にそのデコレートされたwrapperが返される
@deco(z=3)
@deco(z=5)
def func(x, y):
    print(f'exec func:{x=}, {y=}')


if __name__ == '__main__':
    func(1, 2)
