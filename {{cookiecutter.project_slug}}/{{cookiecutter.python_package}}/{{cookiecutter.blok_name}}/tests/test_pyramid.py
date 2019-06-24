import pytest


@pytest.mark.usefixtures('rollback_registry')
class TestPyramidExampleViews:
    """ Test pyramid routes with PyramidBlokTestCase"""

    def test_root(self, webserver):
        """Test pyramid Example get route /"""
        response = webserver.get('/')
        assert response.status == '200 OK'

    def test_examples(self, webserver):
        response = webserver.get('/example')
        assert response.status == '200 OK'
        assert response.json_body == [{'id': 1, 'name': "An example"}]

    def test_get_example(self, webserver):
        response = webserver.get('/example/1', status=200)
        assert response.body.decode('utf8') == "An example"

    def test_post_example(self, webserver):
        response = webserver.post('/example/1', status=404)
        assert response.status == '404 Not Found'
