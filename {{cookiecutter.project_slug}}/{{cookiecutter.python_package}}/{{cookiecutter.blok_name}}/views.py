from pyramid.view import view_config
from pyramid.response import Response

@view_config(route_name='example')
def example_get(request):
    """http get view example.
    See http://doc.anyblok-pyramid.anyblok.org/en/latest/MEMENTO.html#memento
    and https://trypyramid.com for more examples
    """
    return Response("Hello world!")
