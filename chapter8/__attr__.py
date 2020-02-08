class Hoge:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __setattr__(self, name, value):
        # xかy以外の属性を指定するとエラーとなる
        if name not in ("x", "y"):
            raise AttributeError("Not Allowed")
        return super().__setattr__(name, value)

    def __delattr__(self, name):
        # xかyを削除しようとするとエラーとなる
        if name in ("x", "y"):
            raise AttributeError("Not Allowed")
        return super().__delattr__(name)


hoge = Hoge(1, 2)
hoge.hoge = "hoge"
del hoge.x
