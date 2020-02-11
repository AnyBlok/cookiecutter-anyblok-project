#!/bin/bash

{%- if not ('pyramid' == cookiecutter.http_server or 'no' != cookiecutter.furetui) %}
rm -v {{cookiecutter.python_package}}/{{cookiecutter.blok_name}}/views.py
rm -v {{cookiecutter.python_package}}/{{cookiecutter.blok_name}}/tests/test_pyramid.py
{%- endif %}

{%- if 'custom' != cookiecutter.furetui %}
rm -vr src
rm -vr public
rm -vr tests
rm -v package.json
rm -v babel.config.js
rm -v vue.config.js
rm -v .env
rm -v .env.development
{%- endif %}
