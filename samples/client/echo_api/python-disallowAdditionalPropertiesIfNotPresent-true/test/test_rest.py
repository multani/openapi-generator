import unittest
from unittest.mock import patch

from openapi_client.rest import RESTClientObject
from openapi_client.configuration import Configuration



class TestRESTClient(unittest.TestCase):
    def setUp(self):
        pass

    def test_1(self):
        config = Configuration()
        client = RESTClientObject(config)
        url = "http://localhost/test"

        class FakeResponse:
            def __init__(self, status, reason, data):
                self.status = status
                self.reason = reason
                self.data = data

        with patch.object(client.pool_manager, "request") as mock:
            mock.return_value = FakeResponse(200, "OK", "hello")
            response = client.get_request(url)

        self.assertEqual(response.data, "hello")
        self.assertEqual(response.status, 200)
        mock.assert_called_once_with("GET", url)
