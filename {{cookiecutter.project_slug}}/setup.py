#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Setup script for {{ cookiecutter.project_slug }}"""

from setuptools import setup, find_packages
import os


here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.rst'), 'r', encoding='utf-8') as readme_file:
    readme = readme_file.read()

with open(os.path.join(here, 'CHANGELOG.rst'), 'r', encoding='utf-8') as changelog_file:
    changelog = changelog_file.read()

with open(os.path.join(here, 'VERSION'), 'r', encoding='utf-8') as version_file:
    version = version_file.read().strip()

requirements = [
    'anyblok',
    {%- if cookiecutter.db_driver_name == 'postgresql' %}
    'psycopg2',
    {%- endif %}
    {%- if 'anyblok_pyramid' in cookiecutter.http_server.split('+')%}
    'anyblok_pyramid',
    {%- if 'gunicorn' in cookiecutter.http_server.split('+')%}
    'gunicorn',
    {%- endif %}
    {%- endif %}
]

test_requirements = [
    # TODO: put package test requirements here
]

{%- set license_classifiers = {
    'MIT license': 'License :: OSI Approved :: MIT License',
    'BSD license': 'License :: OSI Approved :: BSD License',
    'ISC license': 'License :: OSI Approved :: ISC License (ISCL)',
    'Apache Software License 2.0': 'License :: OSI Approved :: Apache Software License',
    'GNU General Public License v3': 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
} %}

setup(
    name='{{ cookiecutter.python_package }}',
    version=version,
    description="{{ cookiecutter.project_short_description }}",
    long_description=readme + '\n\n' + changelog,
    author="{{ cookiecutter.full_name.replace('\"', '\\\"') }}",
    author_email='{{ cookiecutter.email }}',
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}',
    packages=find_packages(),
    entry_points={
        'bloks': [
            '{{ cookiecutter.blok_name }}={{ cookiecutter.python_package }}.{{ cookiecutter.blok_name }}:{{ cookiecutter.blok_name.capitalize() }}'
            ]
    },
    include_package_data=True,
    install_requires=requirements,
{%- if cookiecutter.open_source_license in license_classifiers %}
    license="{{ cookiecutter.open_source_license }}",
{%- endif %}
    zip_safe=False,
    keywords='{{ cookiecutter.project_slug }}',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
{%- if cookiecutter.open_source_license in license_classifiers %}
        '{{ license_classifiers[cookiecutter.open_source_license] }}',
{%- endif %}
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements,
)
