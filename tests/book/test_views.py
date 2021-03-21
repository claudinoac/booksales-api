from tests.base import BaseDBTestCase
from book.views import Book
import json


class BookTestCase(BaseDBTestCase):
    def setUp(self):
        super(BookTestCase, self).setUp()
        xuxu=Book(title="xainiro")
        self.session.add(
            xuxu
        )
        self.session.commit()

    def test_my_dummy_test(self):
        expected_response = {
            'items': [{
                'id': 1,
                'title': 'xainiro',
                'year': None,
                'price': None,
                'author': None,
                'ISBN': None,
                'language': None
            }]
        }
        response = self.fetch("/book/list")
        response_data = json.loads(response.body)
        self.assertEqual(response_data, expected_response)

    def test_my_new_test(self):
        expected_response = {
            'id': 1,
            'title': 'xainiro',
            'year': None,
            'price': None,
            'author': None,
            'ISBN': None,
            'language': None
        }
        response = self.fetch("/book/1")
        response_data = json.loads(response.body)
        self.assertEqual(response_data, expected_response)
