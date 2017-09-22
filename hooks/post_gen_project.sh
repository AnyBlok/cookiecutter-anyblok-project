#!/bin/bash

{%- if cookiecutter.http_server != 'anyblok_pyramid' %}
rm -v {{cookiecutter.python_package}}/{{cookiecutter.blok_name}}/views.py
{%- endif %}
