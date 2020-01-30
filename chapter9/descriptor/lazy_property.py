class LazyProperty:
    def __init__(self, func):
        self.func = func
        self.name = func.__name__

    def __get__(self, instance, owner):
        # Bookのprice()
        print(self.func)

        # price()
        print(self.name)

        # Bookオブジェクト
        print(instance)

        # クラス変数としてアクセスされた時の処理
        if not instance:
            return self

        # self.funcは関数なので明示的にインスタンスに渡す
        # price(self)となるようにinstanceを引数に指定
        v = self.func(instance)

        # インスタンス変数に関数の結果を格納
        # 2回目以降の呼び出しではインスタンス変数がすでに
        # 定義されていることになり、__get__()は呼び出されない
        instance.__dict__[self.name] = v

        return v


TAX_RATE = 1.10


class Book:
    def __init__(self, raw_price):
        self.raw_price = raw_price

    @LazyProperty
    def price(self):
        print('calculate the price')
        return int(self.raw_price * TAX_RATE)


if __name__ == '__main__':
    book = Book(1980)
    # 計算が初回のみしか行われない
    print(book.price)

    print(book.price)