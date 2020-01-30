class TextField:
    """
    優先度はインスタンス変数よりも低く設定されるため
    同じ名前のインスタンス変数がある場合はそちらが利用され
    __get__()は呼ばれない
    """

    # __set__()を持たないため初期化時に値を受ける
    def __init__(self, value):
        if not isinstance(value, str):
            raise AttributeError('must be str')
        self.value = value

    def __set__name(self, owner, name):
        print(f'__set__name was called')
        print(f'{owner=}, {name=}')
        self.name = name

    def __get__(self, instance, owner):
        print('__get__ was called')
        return self.value

class Book:
    # 初期化時にデータを渡す
    title = TextField('Python Practice Book')


if __name__ == '__main__':
    book = Book()

    # 代入前の取得時には__get__()が呼ばれる
    print(book.title)

    # 代入すると同名のインスタンス変数が定義される
    book.title = 'Book'

    # 同名のインスタンス変数があると__get__()は呼ばれない
    print(book.title)