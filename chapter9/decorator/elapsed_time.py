from functools import wraps
import time


def elapsed_time(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = time.time()
        f(*args, **kwargs)
        print(f'{f.__name__}: {time.time() - start}')
    return wrapper

@elapsed_time
def sample():
    for i in range(100):
        pass


if __name__ == '__main__':
    sample()