{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}
{% for _ in cookiecutter.project_name %}={% endfor %}
{{ cookiecutter.project_name }}
{% for _ in cookiecutter.project_name %}={% endfor %}

{{ cookiecutter.project_short_description }}

{% if is_open_source %}
* Free software: {{ cookiecutter.open_source_license }}
* Documentation: https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io.
{% endif %}

Features
--------

* TODO

Credits
---------

.. _`Anyblok`: https://github.com/AnyBlok/AnyBlok

This `Anyblok`_ package was created with `audreyr/cookiecutter`_ and the `franckbret/cookiecutter-anyblok-project`_ project template.

.. _`franckbret/cookiecutter-anyblok-project`: https://github.com/franckbret/cookiecutter-anyblok-project
.. _`audreyr/cookiecutter`: https://github.com/audreyr/cookiecutter
