import logging
from contextlib import contextmanager

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())

logger.setLevel(logging.INFO)

# ログレベル一時変更と戻す処理を行う
@contextmanager
def debug_context():
    level = logger.level

    try:
        # ログレベルを変更する
        logger.setLevel(logging.DEBUG)
        yield
    finally:
        # 元のログレベルに戻す
        logger.setLevel(level)


def main():
    logger.info('before: info log')
    logger.debug('before: debug log')

    # withブロック内に限っては一時的にログレベルをDEBUGまで引き下げている
    with debug_context():
        logger.info('inside the block: info log')
        logger.debug('inside the block: debug log')

    logger.info('after: info log')
    logger.debug('after: debug log')


if __name__ == '__main__':
    main()