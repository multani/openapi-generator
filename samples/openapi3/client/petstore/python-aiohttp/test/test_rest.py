import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
import unittest
from unittest.mock import patch
from unittest.mock import AsyncMock

from petstore_api.rest import RESTClientObject
from petstore_api.configuration import Configuration


class FakeResponse:
    def __init__(self, status, reason, data):
        self.status = status
        self.reason = reason
        self._data = data

    async def read(self):
        return self._data





class TestRESTClient(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        class Handler(BaseHTTPRequestHandler):
            pass

        server_address = ('', 8000)
        self.httpd = HTTPServer(server_address, Handler)

        self.thread = threading.Thread(target=self.httpd.serve_forever)
        self.thread.start()

    def tearDown(self):
        print("shutting down")
        self.httpd.shutdown()
        self.thread.join()
        print("shut down")


    async def test_get(self):
        config = Configuration()
        client = RESTClientObject(config)
        url = "http://localhost:8000"


        class Handler(BaseHTTPRequestHandler):
            def do_GET(self):
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b"hello")
        
        self.httpd.RequestHandlerClass = Handler

        # with patch.object(client.pool_manager, "request", new=AsyncMock()) as mock:
            # mock.return_value = FakeResponse(200, "OK", "hello")
        response = await client.get_request(url)

        self.assertEqual(response.data, b"hello")
        self.assertEqual(response.status, 200)
        # mock.assert_called_once_with("GET", url, timeout=300, headers={'Content-Type': 'application/json'})


    async def test_post(self):
        config = Configuration()
        client = RESTClientObject(config)
        url = "http://localhost/test"

        with patch.object(client.pool_manager, "request", new=AsyncMock()) as mock:
            mock.return_value = FakeResponse(200, "OK", "hello")
            response = await client.post_request(url)

        self.assertEqual(response.data, "hello")
        self.assertEqual(response.status, 200)
        mock.assert_called_once_with("POST", url, timeout=300, headers={'Content-Type': 'application/json'}, data=None)


    async def test_post_with_params(self):
        config = Configuration()
        client = RESTClientObject(config)
        url = "http://localhost/test"

        with patch.object(client.pool_manager, "request", new=AsyncMock()) as mock:
            mock.return_value = FakeResponse(200, "OK", "hello")
            response = await client.post_request(url, post_params=[("foo", "bar")])

        self.assertEqual(response.data, "hello")
        self.assertEqual(response.status, 200)
        mock.assert_called_once_with("POST", url, timeout=300, headers={'Content-Type': 'application/json'}, data=None)
