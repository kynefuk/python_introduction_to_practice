import base64
import sys


def str_to_base64(string):

    return base64.b64encode(string.encode("utf-8"))


if __name__ == "__main__":
    target = sys.argv[1]
    print(str_to_base64(target))
