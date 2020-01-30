from hashlib import md5
from pathlib import Path
from urllib import request
import time


urls = [
    'https://twitter.com',
    'https://facebook.com',
    'https://instagram.com'
]


def download(url):
    req = request.Request(url)
    name = md5(url.encode('utf-8')).hexdigest()
    file_path = './' + name

    with request.urlopen(req) as res:
        Path(file_path).write_bytes(res.read())
        return url, file_path


def elapsed_time(f):
    def wrapper(*args, **kwargs):
        start = time.time()
        v = f(*args, **kwargs)
        print(f'{f.__name__}: {time.time() - start}')
        return v
    return wrapper


# 逐次処理
@elapsed_time
def get_sequential():
    for url in urls:
        print(download(url))


if __name__ == '__main__':
    get_sequential()