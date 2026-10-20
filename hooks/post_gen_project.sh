#!/bin/bash

{%- if cookiecutter.http_server == 'no' and cookiecutter.feretui == 'no' and cookiecutter.furetui == 'no' %}
rm -vf {{cookiecutter.python_package}}/{{cookiecutter.blok_name}}/views.py
rm -vf {{cookiecutter.python_package}}/{{cookiecutter.blok_name}}/tests/test_pyramid.py
{%- endif %}

{%- if cookiecutter.http_server != 'pyramid' %}
rm -vf {{cookiecutter.python_package}}/{{cookiecutter.blok_name}}/tests/test_pyramid.py
{%- endif %}

{%- if cookiecutter.feretui != 'yes' %}
rm -vf {{cookiecutter.python_package}}/{{cookiecutter.blok_name}}/resources.py
{%- endif %}

{%- if 'custom' != cookiecutter.furetui %}
rm -vrf src
rm -vrf public
rm -vrf tests
rm -vf package.json
rm -vf babel.config.js
rm -vf vue.config.js
rm -vf .env
rm -vf .env.development
{%- endif %}
