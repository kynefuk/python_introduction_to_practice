from collections import defaultdict


class CountDict:
    def __init__(self, *args, **kwargs):
        self._data = {}
        self._get_count = defaultdict(int)
        self._set_count = defaultdict(int)

    def __getitem__(self, key):
        self._get_count[key] += 1
        return self._data[key]

    def __setitem__(self, key, value):
        self._set_count[key] += 1
        self._data[key] = value

    @property
    def count(self):
        return {
            f"set: {list(self._set_count.items())}",
            f"get: {list(self._get_count.items())}",
        }


c = CountDict()
c["x"] = 1
print(c["x"])

c["x"] = 100
c["y"] = 2
print(c["y"])

print(c.count)
