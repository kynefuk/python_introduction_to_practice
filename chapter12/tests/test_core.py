import pathlib
import unittest
from tempfile import TemporaryDirectory
from unittest.mock import patch
from urllib.error import URLError


THUMBNAIL_URL = (
    'http://books.google.com/books/content'
    '?id=OgtBw760Y5EC&printsec=frontcover'
    '&img=1&zoom=1&edge=curl&source=gbs_api'
)


class SaveThumbnailsTest(unittest.TestCase):
    def setUp(self):
        # 一時ディレクトリの作成
        self.tmp = TemporaryDirectory()

    def tearDown(self):
        # 一時ディレクトリの削除
        self.tmp.cleanup()

    # 指定したオブジェクトをモックオブジェクトに切り替える
    # デコレータの場合は呼び出し時の引数に置き換え後のモックオブジェクトが渡される
    @patch('booksearch.core.get_data')
    def test_save_thumbnails(self, mock_get_data):
        from booksearch.core import Book

        data_path = pathlib.Path(__file__).with_name('data')

        # モックオブジェクトの振る舞いを指定
        mock_get_data.return_value = (
            data_path / 'oW63DwAAQBAJ_smallThumbnail.jpeg'
        ).read_bytes()

        book = Book({'id': '', 'volumeInfo': {
            'imageLinks': {
                'thumbnail': THUMBNAIL_URL
            }
        }})

        filename = book.save_thumbnails(self.tmp.name)[0]

        mock_get_data.assert_called_with(THUMBNAIL_URL)

        data = pathlib.Path(data_path / 'oW63DwAAQBAJ_smallThumbnail.jpeg').read_bytes()

        self.assertEqual(data, filename.read_bytes())


class GetBooksTest(unittest.TestCase):
    def test_get_books_no_connection(self):
        from booksearch.core import get_books

        with patch('socket.socket.connect') as mock:
            mock.return_value = None

            with self.assertRaisesRegex(URLError, 'urlopen error'):
                # 例外が発生する処理をWithブロック内で実行する
                get_books(q='python')