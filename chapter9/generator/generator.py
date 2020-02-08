def gen_func(num):
    print("start")
    while num:
        print(f"yield: {num}")
        yield num  # ここで一時中断される
        num -= 1


gen = gen_func(2)
print(gen)

for i in gen_func(2):
    print(i)

print(max(i for i in gen_func(3)))


def gen():
    for i in range(3):
        yield i
    for i in range(5):
        yield i


for i in gen():
    print(i)

# yield fromでコードを小さくできる
def gen_from():
    yield from (i for i in range(3))
    yield from (i for i in range(5))


for i in gen_from():
    print(i)
