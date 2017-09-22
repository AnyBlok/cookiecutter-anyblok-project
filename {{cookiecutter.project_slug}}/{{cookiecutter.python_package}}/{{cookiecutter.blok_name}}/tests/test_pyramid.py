from anyblok_pyramid.tests.testcase import PyramidBlokTestCase


class TestCanigooRestApi(PyramidBlokTestCase):
    """ Test pyramid routes with PyramidBlokTestCase"""

    def test_example_get(self):
        """Test pyramid Example get route /"""
        response = self.webserver.get('/')
        self.assertEqual(response.status, '200 OK')
