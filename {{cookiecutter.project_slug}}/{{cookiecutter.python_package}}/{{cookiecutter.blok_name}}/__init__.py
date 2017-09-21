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
