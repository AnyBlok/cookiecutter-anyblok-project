from pyramid.view import view_defaults, view_config
from anyblok_pyramid import current_blok
from pyramid.response import Response


@view_defaults(installed_blok=current_blok())
class ExampleView:
    def __init__(self, request):
        self.request = request
        self.registry = request.anyblok.registry

    @view_config(route_name='example')
    def example_get(self):
        """http get view example.
        See
        http://doc.anyblok-pyramid.anyblok.org/en/latest/MEMENTO.html#memento
        and https://trypyramid.com for more examples
        """
        return Response("Hello world!")
