from tornado.testing import AsyncHTTPTestCase


class HTTPTest(AsyncHTTPTestCase):
    def test_http_fetch(self):
        response = self.fetch("/match", method="POST")
        self.assertEqual(response.code, 200)
