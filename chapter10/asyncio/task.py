import asyncio


async def coro(n):
    await asyncio.sleep(n)
    return n


async def main():
    # タスクは実行がスケジューリングされたコルーチンをカプセル化したもの
    task1 = asyncio.create_task(coro(1))
    task2 = asyncio.create_task(coro(2))
    task3 = asyncio.create_task(coro(3))

    # awaitを使って実行し、同期処理のように戻り値を取得できる。
    print(await task1)
    print(await task2)
    print(await task3)

if __name__ == '__main__':
    asyncio.run(main())
