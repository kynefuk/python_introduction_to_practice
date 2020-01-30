import asyncio
import random


async def call_web_api(url):
    # Web APIコールをスリープで代用
    print(f'send a request: {url}')

    # awaitでこの処理が終わるまでコルーチンを中断する
    await asyncio.sleep(random.random())

    print(f'got a response: {url}')
    return url


async def async_download(url):
    # awaitを使ってコルーチンを呼び出す
    # awaitキーワードがないとコルーチンオブジェクトが生成されるだけで
    # 実行までは行われない事に注意
    response = await call_web_api(url)
    return response


async def main():
    # gatherに渡した順にasync_downloadが実行される
    # 処理中のsleep()で処理が中断され、次のコルーチンが実行される
    # その後はsleepが終わったコルーチンから順次処理が再開される。
    task = asyncio.gather(
        async_download('https://twitter.com/'),
        async_download('https://facebook.com/'),
        async_download('https://instagram.com/')
    )

    # gather()の戻り値はawaitableなオブジェクトなので
    # awaitキーワードが必要となる
    return await task


if __name__ == '__main__':
    result = asyncio.run(main())

    # twitter, facebook, instagramの順を保持してくれる
    print(result)
