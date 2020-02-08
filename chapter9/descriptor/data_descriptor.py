class TextField:
    # title = TextField()で呼び出される
    def __set_name__(self, owner, name):
        print(f'__set__name was called')
        print(f'{owner=}, {name=}')
        self.name = name

    # setter
    def __set__(self, instance, value):
        print('__set__ was called')
        if not isinstance(value, str):
            raise AttributeError('must be str')

        # instance(book)の属性(name)に値を設定する
        # instance.と書いてしまうと__set__が再帰的に呼び出されてしまう
        instance.__dict__[self.name] = value

    # getter
    def __get__(self, instance, owner):
        print('__get__ was called')

        # instance(book)の属性(name)を返す
        return instance.__dict__[self.name]


class Book:
    title = TextField()


if __name__ == '__main__':
    book = Book()
    # __set__が呼び出される
    book.title = 'Python Practice Book'

    # __get__が呼び出される
    print(book.title)