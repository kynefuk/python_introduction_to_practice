from functools import wraps

def deco4(f):
    # wrapsを使う事で実際に実行される関数の名前や
    # Docstringを元の関数のものに置き換える事ができる
    @wraps(f)

    def wrapper(*args, **kwargs):
        print('before exec')
        f(*args, **kwargs)
        print(f'{f.__name__}')
        print('after exec')
    return wrapper


@deco4
def sample():
    print('exec')



if __name__ == '__main__':
    sample()