from tornado.testing import AsyncHTTPTestCase
from server import make_app

class HTTPTest(AsyncHTTPTestCase):
    def get_app(self):
        return make_app()

    def test_http_fetch(self):
        response = self.fetch("/match", method="POST",body="")
        self.assertEqual(response.code, 200)
