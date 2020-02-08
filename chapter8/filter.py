x = (1, 4, 3, 5, 2)

# イテラブルの要素を条件で絞り込みを行う
filtered_x = list(filter(lambda x: x > 3, x))

print(filtered_x)


# イテラブルの全ての要素に処理を行う
mapped_x = list(map(lambda x: x * 2, x))
print(mapped_x)


keys = ("q", "limit", "page")
values = ("python", "10", "100")

query_param = list(map(lambda k, v: f"{k}={v}", keys, values))
query = "?" + "&".join(query_param)
print(query)
