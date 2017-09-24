#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Setup script for my_project"""

from setuptools import setup, find_packages
import os


here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.rst'), 'r', encoding='utf-8') as readme_file:
    readme = readme_file.read()

with open(os.path.join(here, 'CHANGELOG.rst'), 'r', encoding='utf-8') as changelog_file:
    changelog = changelog_file.read()

requirements = [
    'anyblok',
    'psycopg2',
    'anyblok_pyramid',
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='my_project',
    version='0.1.0',
    description="AnyBlok test",
    long_description=readme + '\n\n' + changelog,
    author="Jean-Sébastien Suzanne",
    author_email='jssuzanne@anybox.fr',
    url='https://github.com/jssuzanne/my_project',
    packages=find_packages(),
    entry_points={
        'bloks': [
            'blok1=my_project.blok1:Blok1'
            ]
    },
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    keywords='my_project',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
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
