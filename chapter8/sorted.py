from operator import attrgetter, itemgetter


x = ["1", "4", 3, 1, 2]

# keyに引数を1つだけ取る関数を指定
# ソートが行われる際に、この関数に各要素が渡され、
# 比較に利用する値を返す
sorted_x = sorted(x, key=lambda x: int(x))
print(sorted_x)


counts = [
    {"word": "python", "count": 3},
    {"word": "practice", "count": 5},
    {"word": "hoge", "count": 1},
]

sorted_counts = sorted(counts, key=itemgetter("count"), reverse=True)
print(sorted_counts)


class Hoge:
    def __init__(self, num):
        self.num = num

    def __str__(self):
        return self.num

    def __repr__(self):
        return str(self.num)


lis = []
for _ in range(5):
    hoge = Hoge(_)
    lis.append(hoge)


sorted_list = sorted(lis, key=attrgetter("num"))
print(sorted_list)
