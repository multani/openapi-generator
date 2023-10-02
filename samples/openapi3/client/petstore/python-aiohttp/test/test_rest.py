import unittest
from unittest.mock import patch
from unittest.mock import AsyncMock

from petstore_api.rest import RESTClientObject
from petstore_api.configuration import Configuration



class TestRESTClient(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        pass

    async def test_1(self):
        config = Configuration()
        client = RESTClientObject(config)
        url = "http://localhost/test"

        class FakeResponse:
            def __init__(self, status, reason, data):
                self.status = status
                self.reason = reason
                self._data = data

            async def read(self):
                return self._data

        with patch.object(client.pool_manager, "request", new=AsyncMock()) as mock:
            mock.return_value = FakeResponse(200, "OK", "hello")
            response = await client.get_request(url)

        self.assertEqual(response.data, "hello")
        self.assertEqual(response.status, 200)
        mock.assert_called_once_with("GET", url)
