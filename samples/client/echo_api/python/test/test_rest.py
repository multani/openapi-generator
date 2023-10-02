import unittest
from unittest.mock import patch

from openapi_client.rest import RESTClientObject
from openapi_client.configuration import Configuration


class FakeResponse:
    def __init__(self, status, reason, data):
        self.status = status
        self.reason = reason
        self.data = data


class TestRESTClient(unittest.TestCase):
    def setUp(self):
        pass

    def test_get(self):
        config = Configuration()
        client = RESTClientObject(config)
        url = "http://localhost/test"

        with patch.object(client.pool_manager, "request") as mock:
            mock.return_value = FakeResponse(200, "OK", "hello")
            response = client.get_request(url)

        self.assertEqual(response.data, "hello")
        self.assertEqual(response.status, 200)
        mock.assert_called_once_with("GET", url, preload_content=True, timeout=None, headers={})


    def test_post(self):
        config = Configuration()
        client = RESTClientObject(config)
        url = "http://localhost/test"

        with patch.object(client.pool_manager, "request") as mock:
            mock.return_value = FakeResponse(200, "OK", "hello")
            response = client.post_request(url)

        self.assertEqual(response.data, "hello")
        self.assertEqual(response.status, 200)
        mock.assert_called_once_with("POST", url, preload_content=True, timeout=None, headers={}, body=None)


    def test_post_with_params(self):
        config = Configuration()
        client = RESTClientObject(config)
        url = "http://localhost/test"

        with patch.object(client.pool_manager, "request") as mock:
            mock.return_value = FakeResponse(200, "OK", "hello")
            response = client.post_request(url, post_params={"foo": "bar"})

        self.assertEqual(response.data, "hello")
        self.assertEqual(response.status, 200)
        mock.assert_called_once_with("POST", url, preload_content=True, timeout=None, headers={}, body=None, fields={"foo": "bar"})
