#!/bin/bash

{%- if 'anyblok_pyramid' not in cookiecutter.http_server.split('+') %}
rm -v {{cookiecutter.python_package}}/{{cookiecutter.blok_name}}/views.py
rm -v {{cookiecutter.python_package}}/{{cookiecutter.blok_name}}/tests/test_pyramid.py
{%- endif %}
