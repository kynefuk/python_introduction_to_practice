def deco1(f):
    print('deco1 called')

    # デコレート対象の関数fの前後でログ出力する
    # 名前はwrapperじゃなくても良い
    def wrapper():
        print('before exec')
        f() #元の関数を実行
        print('after exec')

    # deco1はwrapper()を元の関数に返すので
    # プログラムの実行中に元の関数が呼び出されると、
    # 元の関数の代わりにwrapper()が実行される。
    return wrapper


# デコレータは関数定義時に実行される
# sample()はdeco1が返すwrapper()に置き換わるので
# sample()の実行はwrapper()の呼び出しとなる
@deco1
def sample():
    print('sample called')


if __name__ == '__main__':
    sample()