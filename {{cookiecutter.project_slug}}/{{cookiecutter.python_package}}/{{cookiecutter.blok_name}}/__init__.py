"""Blok declaration example
"""
from anyblok.blok import Blok


class {{ cookiecutter.blok_name.capitalize() }}(Blok):
    """{{ cookiecutter.blok_name.capitalize() }}'s Blok class definition
    """
    version = "{{ cookiecutter.version }}"
    required = ['anyblok-core']

    @classmethod
    def import_declaration_module(cls):
        """Python module to import in the given order at start-up
        """
        from . import model  # noqa

    @classmethod
    def reload_declaration_module(cls, reload):
        """Python module to import while reloading server (ie when
        adding Blok at runtime
        """
        from . import model  # noqa
        reload(model)
    {%- if cookiecutter.http_server == 'anyblok_pyramid' %}

    @classmethod
    def pyramid_load_config(cls, config):
        config.add_route("example", "/")
        config.scan(cls.__module__ + '.views')
    {%- endif %}
