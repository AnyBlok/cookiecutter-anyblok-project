.. image:: https://travis-ci.org/AnyBlok/cookiecutter-anyblok-project.svg?branch=master
    :target: https://travis-ci.org/AnyBlok/cookiecutter-anyblok-project
    :alt: Build status

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


  :project_name: "Project name"
  :project_slug: "project-name", used by repository/directory name
  :project_short_description: "A short description of the Anyblok based project"
  :python_package: "project_name", the python package name
  :blok_name: "project_name", the blok name
  :db_driver_name: "postgresql", the database driver name, AnyBlok use SqlAlchemy
  :db_name: "project_name", the database name
  :http_server: [
        "no", 
        "anyblok_pyramid", 
        "anyblok_pyramid+gunicorn"
    ], anyblok_pyramid will add a pyramid http server
  :open_source_license: ["Mozilla Public License Version 2.0", "GNU General Public License v3", "MIT license", "BSD license", "ISC license", "Apache Software License 2.0", "Not open source"]
  :version: "0.1.0"
  :full_name: "Your name"
  :email: "you@example.com"
  :github_username: "github_username"

Common commands
---------------

Once you have generated a project, you can see a list of common commands running.

    `make help`

Please note that you need to have to be within an activated virtualenv to launch those commands.

    `make setup-dev`

Will install python dependencies, create a new database and install the blok. 
You can then run "anyblok_interpreter -c app.dev.config" to access the interactive python
api (See `Anyblok Book`_ to dive in AnyBlok concepts)

    `make setup-tests`

Will install python testing dependencies and create a test database.

    `make test`

Will run unit tests.

    `make lint`

Will run flake8.

    `make run-dev`

If you choose to install `anyblok_pyramid`, it will run a webserver on localhost:8080.

.. _`Anyblok Book`: https://anyblok.gitbooks.io/anyblok-book/content/

Credits
---------

This `Anyblok`_ package was created with `audreyr/cookiecutter`_ and the `AnyBlok/cookiecutter-anyblok-project`_ project template.

.. _`Anyblok`: https://github.com/AnyBlok/AnyBlok
.. _`AnyBlok/cookiecutter-anyblok-project`: https://github.com/Anyblok/cookiecutter-anyblok-project
.. _`audreyr/cookiecutter`: https://github.com/audreyr/cookiecutter

License
-------

.. _`Mozilla Public License Version 2.0`: https://www.mozilla.org/en-US/MPL/2.0/

This project is licensed under the terms of the `Mozilla Public License Version 2.0`_
