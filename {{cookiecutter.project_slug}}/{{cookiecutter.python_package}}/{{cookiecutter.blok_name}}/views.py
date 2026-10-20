{%- if 'pyramid' == cookiecutter.http_server %}
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
            <a href="./example">List all available examples</a><br/>
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
        """view all examples."""
        return self.registry.Example.query().all().to_dict()
{%- elif 'fastapi' == cookiecutter.http_server %}
from fastapi import APIRouter
from anyblok_fastapi.crud import get_crud_router
from anyblok import Declarations

router = APIRouter(prefix="/api")


@router.get("/")
def api_root():
    return {"message": "Welcome to {{ cookiecutter.project_name }} API"}


def get_router(registry):
    crud_router = get_crud_router(
        model=Declarations.Model.Example,
        registry=registry,
        prefix="/examples",
        tags=["Examples"],
    )
    router.include_router(crud_router)
    return router
{%- elif 'starlette' == cookiecutter.http_server %}
from starlette.responses import JSONResponse, PlainTextResponse
from starlette.routing import Route


async def homepage(request):
    return PlainTextResponse("Welcome to {{ cookiecutter.project_name }}")


async def list_examples(request):
    registry = request.state.anyblok_registry
    examples = registry.Example.query().all()
    return JSONResponse([{"id": e.id, "name": e.name} for e in examples])


routes = [
    Route("/", homepage, methods=["GET"]),
    Route("/examples", list_examples, methods=["GET"]),
]
{%- endif %}
