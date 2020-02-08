class Mutable:
    def __init__(self, attr_map):
        for k, v in attr_map.items():
            setattr(self, str(k), v)

    def do_something(self):
        return "do something"


m = Mutable({"a": 1, "b": 2})
print(m.a)
print(getattr(m, "b"))

# getattrでMutableインスタンスの関数オブジェクトを取得
instance_method = getattr(m, "do_something")
print(instance_method())
