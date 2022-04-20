import json
import unittest
from unittest.mock import patch, MagicMock

from getting_weather import get_weather, GOOD, BAD


class GettingWeatherTest(unittest.TestCase):

    @patch('getting_weather.requests')
    def test_good(self, requests_mock):

        with open('openweathermap.org_example_response.json', 'r') as f:
            body = json.load(f)

        request_respone_mock = MagicMock()
        request_respone_mock.status_code = 200
        request_respone_mock.json.return_value = body

        requests_mock.get.return_value = request_respone_mock

        self.assertEqual(GOOD, get_weather('Dubai'))

    @patch('getting_weather.requests')
    def test_bad(self, requests_mock):
        request_respone_mock = MagicMock()
        request_respone_mock.status_code = 200
        request_respone_mock.json.return_value = {'main': {'temp': 17}}

        requests_mock.get.return_value = request_respone_mock

        self.assertEqual(BAD, get_weather('Kharkov'))

    @patch('getting_weather.requests')
    def test_error_from_server(self, requests_mock):
        request_respone_mock = MagicMock()
        request_respone_mock.status_code = 404
        request_respone_mock.json.return_value = {'message': "City not found"}
        requests_mock.get.return_value = request_respone_mock

        with self.assertRaises(RuntimeError):
            get_weather('Kharkov')
