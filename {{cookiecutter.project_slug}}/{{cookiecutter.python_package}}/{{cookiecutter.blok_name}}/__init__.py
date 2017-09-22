from anyblok.blok import Blok


class {{ cookiecutter.blok_name.replace('_', '').capitalize() }}(Blok):
    version = "{{ cookiecutter.version }}"
    required = ['anyblok-core']

    @classmethod
    def import_declaration_module(cls):
        from . import model  # noqa

    @classmethod
    def reload_declaration_module(cls, reload):
        from . import model  # noqa
        reload(model)
    {%- if cookiecutter.http_server == 'anyblok_pyramid' %}

    @classmethod
    def pyramid_load_config(cls, config):
        config.add_route("example", "/")
        config.scan(cls.__module__ + '.views')
    {%- endif %}
