.. {{ cookiecutter.project_name }} documentation master file, created by
   sphinx-quickstart on Fri Sep 22 12:52:36 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to {{ cookiecutter.project_name }}'s documentation!
==========={% for _ in cookiecutter.project_name %}={% endfor %}=================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   apidoc

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
