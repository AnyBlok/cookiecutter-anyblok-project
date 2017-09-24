from anyblok_pyramid.tests.testcase import PyramidBlokTestCase


class TestCanigooRestApi(PyramidBlokTestCase):
    """ Test pyramid routes with PyramidBlokTestCase"""

    def test_root(self):
        """Test pyramid Example get route /"""
        response = self.webserver.get('/')
        self.assertEqual(response.status, '200 OK')

    def test_examples(self):
        response = self.webserver.get('/example')
        self.assertEqual(response.status, '200 OK')
        self.assertEqual(response.json_body, [{'id': 1, 'name': "An example"}])

    def test_get_example(self):
        response = self.webserver.get('/example/1', status=200)
        self.assertEqual(response.body.decode('utf8'), "An example")

    def test_post_example(self):
        response = self.webserver.post('/example/1', status=404)
        self.assertEqual(response.status, '404 Not Found')
