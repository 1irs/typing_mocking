import unittest
from unittest.mock import patch, MagicMock

from database_search import search_db


class DatabaseSearchTest(unittest.TestCase):

    @patch('database_search.create_engine')
    def test(self, create_engine_mock):

        con_mock = MagicMock()
        con_mock.execute.return_value.fetchall.return_value = [
            (1, 'bizibaza-api', 2),
            (2, 'asdf', 3)
        ]

        engine_mock = MagicMock()
        engine_mock.connect.return_value.__enter__.return_value = con_mock

        create_engine_mock.return_value = engine_mock

        res = search_db('bizi')

        self.assertEqual(2, len(res))
        self.assertEqual('bizibaza-api', res[0].name)
