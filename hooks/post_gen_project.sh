#!/bin/bash

{%- if not ('pyramid' == cookiecutter.http_server or 'no' != cookiecutter.furetui) %}
rm -v {{cookiecutter.python_package}}/{{cookiecutter.blok_name}}/views.py
rm -v {{cookiecutter.python_package}}/{{cookiecutter.blok_name}}/tests/test_pyramid.py
{%- endif %}

{%- if 'custom' != cookiecutter.furetui %}
rm -rv {{cookiecutter.python_package}}/backend
{%- endif %}
