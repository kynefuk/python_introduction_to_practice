import asyncio


# async defにすると、戻り値がコルーチンになる
async def coro():
    return 1


if __name__ == '__main__':
    # コルーチンの実行方法は、asyncio.runに渡すこと
    print(asyncio.run(coro()))