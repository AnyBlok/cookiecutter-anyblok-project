"""Blok declaration example
"""
from anyblok.blok import Blok


class {{ cookiecutter.blok_name.capitalize() }}(Blok):
    """{{ cookiecutter.blok_name.capitalize() }}'s Blok class definition
    """
    version = "{{ cookiecutter.version }}"
    author = "{{ cookiecutter.full_name.replace('\"', '\\\"') }}"
    required = [
        'anyblok-core',
        {%- if 'yes' == cookiecutter.feretui %}
        'anyblok-starlette-feretui',
        {%- elif 'no' != cookiecutter.furetui %}
        'furetui',
        {%- endif %}
    ]

    @classmethod
    def import_declaration_module(cls):
        """Python module to import in the given order at start-up
        """
        from . import model  # noqa
        {%- if 'yes' == cookiecutter.feretui %}
        from . import resources  # noqa
        {%- endif %}

    @classmethod
    def reload_declaration_module(cls, reload):
        """Python module to import while reloading server (ie when
        adding Blok at runtime)
        """
        from . import model  # noqa
        reload(model)
        {%- if 'yes' == cookiecutter.feretui %}
        from . import resources  # noqa
        reload(resources)
        {%- endif %}
    {%- if 'pyramid' == cookiecutter.http_server %}

    @classmethod
    def pyramid_load_config(cls, config):
        config.add_route("root", "/")
        config.add_route("example_list", "/example")
        config.add_route("example", "/example/{id}")
        config.scan(cls.__module__ + '.views')
    {%- elif 'fastapi' == cookiecutter.http_server %}

    @classmethod
    def prepare_fastapi(cls, app, registry):
        from .views import get_router
        app.include_router(get_router(registry))
    {%- elif 'starlette' == cookiecutter.http_server %}

    @classmethod
    def prepare_starlette(cls, app, registry):
        from .views import routes
        for route in routes:
            app.routes.append(route)
    {%- endif %}
