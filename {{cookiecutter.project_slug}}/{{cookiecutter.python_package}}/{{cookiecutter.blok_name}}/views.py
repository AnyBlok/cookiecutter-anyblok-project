from pyramid.view import view_defaults, view_config
from anyblok_pyramid import current_blok
from pyramid.response import Response


@view_defaults(installed_blok=current_blok())
class ExampleView:
    def __init__(self, request):
        self.request = request
        self.registry = request.anyblok.registry

    @view_config(route_name='root')
    def route_root(self):
        return Response(
            """
            <a href="./example">List all availaible examples</a><br/>
            <a href="./example/1">Get example id=1</a>
            """
        )

    @view_config(route_name='example', request_method='GET')
    def route_example(self):
        example = self.registry.Example.query().get(
            self.request.matchdict['id']
        )
        return Response(example.name)

    @view_config(route_name='example_list', renderer='json')
    def route_examples(self):
        """view all examples.
        """
        return self.registry.Example.query().all().to_dict()
