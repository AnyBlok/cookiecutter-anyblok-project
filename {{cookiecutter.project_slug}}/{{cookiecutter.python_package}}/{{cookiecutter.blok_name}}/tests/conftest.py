from anyblok.conftest import *  # noqa: F401,F403
{%- if 'anyblok_pyramid' in cookiecutter.http_server.split('+') %}
from anyblok_pyramid.conftest import *  # noqa: F401,F403
{%- endif %}
