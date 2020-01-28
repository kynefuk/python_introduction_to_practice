import sys
import unittest


class BuildUrlTest(unittest.TestCase):
    def test_build_url(self):
        from booksearch.api import build_url
        expected = 'https://www.googleapis.com/books/v1/volumes?q=python'
        actual = build_url({'q': 'python'})

        self.assertEqual(expected, actual)

    def test_build_url_empty_param(self):
        from booksearch.api import build_url

        expected = 'https://www.googleapis.com/books/v1/volumes?'
        actual = build_url({})

        self.assertEqual(expected, actual)

    # 失敗することがわかっている場合のデコレータ
    @unittest.expectedFailure
    def test_build_url_fail(self):
        from booksearch.api import build_url

        expected = 'https://www.googleapis.com/books/v1/volumes'
        actual = build_url({})

        self.assertEqual(expected, actual, msg='このテストは失敗します')

    # テストをスキップ
    @unittest.skip('this is a skip test')
    def test_nothing_skip(self):
        pass

    # 条件に応じてテストをスキップ
    @unittest.skipIf(sys.version_info > (3, 6),
                    'this is a skipIf test')
    def test_nothing_skipIf(self):
        pass


class BuildUrlMultiTest(unittest.TestCase):
    def test_build_url_multi(self):
        from booksearch.api import build_url

        base = 'https://www.googleapis.com/books/v1/volumes?'
        expected_url = f'{base}q=python'
        params = (
            (expected_url, {'q': 'python'}),
            (expected_url, {'q': 'python', 'maxResults': 1}),
            (expected_url, {'q': 'python', 'langRestrict': 'en'})
        )

        for expected, param in params:
            # withブロック1つがテストケース1つに相当する
            with self.subTest(**param):
                actual = build_url(param)
                self.assertEqual(expected, actual)