============================
cookiecutter-anyblok-project
============================

Bootstrap Anyblok based project

Requirements
------------

Install `cookiecutter` command line: 

  `pip install cookiecutter`

Usage
-----

Generate a new Anyblok project template layout: 

  `cookiecutter gh:AnyBlok/cookiecutter-anyblok-project`

You will be prompt with questions to set configuration values.


    "project_name": "Name of the project"
    "project_slug": "name-of-the-project", used by repository/directory name
    "project_short_description": "A short description of the Anyblok based project"
    "release_date": ""
    "python_package": "name_of_the_project", the python package name
    "blok_name": "name_of_the_project", the blok name
    "db_driver_name": "postgresql", the database driver name, AnyBlok use SqlAlchemy
    "db_name": "name_of_the_project", the database name
    "open_source_license": ["Mozilla Public License Version 2.0", "GNU General Public License v3", "MIT license", "BSD license", "ISC license", "Apache Software License 2.0", "Not open source"]
    "version": "0.1.0"
    "full_name": "Your name"
    "email": "you@example.com"
    "github_username": "github_username"


Credits
---------

.. _`Anyblok`: https://github.com/AnyBlok/AnyBlok

This `Anyblok`_ package was created with `audreyr/cookiecutter`_ and the `AnyBlok/cookiecutter-anyblok-project`_ project template.

.. _`AnyBlok/cookiecutter-anyblok-project`: https://github.com/Anyblok/cookiecutter-anyblok-project
.. _`audreyr/cookiecutter`: https://github.com/audreyr/cookiecutter

License
-------

.. _`Mozilla Public License Version 2.0`: https://www.mozilla.org/en-US/MPL/2.0/

This project is licensed under the terms of the `Mozilla Public License Version 2.0`_
