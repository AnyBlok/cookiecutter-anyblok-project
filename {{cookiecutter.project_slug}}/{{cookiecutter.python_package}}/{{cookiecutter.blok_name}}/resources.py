from anyblok import Declarations
from anyblok_starlette_feretui.resource import AnyBlokModelResource


@Declarations.register(Declarations.FeretUI.admin)
class ExampleResource(AnyBlokModelResource):
    code = "examples"
    label = "Examples"
    model = Declarations.Model.Example
    views = ["list", "read", "create", "update", "delete"]
