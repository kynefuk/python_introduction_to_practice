class Reverser:
    def __init__(self, lis):
        self.lis = lis

    def __iter__(self):
        # iterは__iter__と__next__を実装しているイテレータを返す必要がある
        # for文はこの__iter__を呼び出しその戻り値のイテレータを利用する
        return self

    def __next__(self):
        # ループの度に呼ばれ、戻り値がループの変数に渡される
        # __next__は返す値がなくなった場合はStopIterationを投げる必要がある
        try:
            return self.lis.pop()
        except IndexError:
            raise StopIteration


lis = [val for val in Reverser([1, 2, 3])]
print(lis)
