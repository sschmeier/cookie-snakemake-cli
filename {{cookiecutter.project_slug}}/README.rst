{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}
{% for _ in cookiecutter.project_name %}={% endfor %}
{{ cookiecutter.project_name }}
{% for _ in cookiecutter.project_name %}={% endfor %}

{% if is_open_source %}
.. image:: https://img.shields.io/travis/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.svg
        :target: https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}

.. image:: https://readthedocs.org/projects/{{ cookiecutter.project_slug | replace("_", "-") }}/badge/?version=latest
        :target: https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status
{%- endif %}

{% if cookiecutter.add_pyup_badge == 'y' %}
.. image:: https://pyup.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/shield.svg
     :target: https://pyup.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/
     :alt: Updates
{% endif %}


{{ cookiecutter.project_short_description }}

This example bundles the Snakefile with the
command line tool, but this tool can also look
in the user's working directory for Snakefiles.

Snakemake functionality is provided through
a command line tool called `{{cookiecutter.project_slug}}`.

Quickstart
----------

This runs through the installation and usage
of `{{cookiecutter.project_slug}}`.

Quick install
-------------

Start by setting up a conda environment,
and install the required packages into the
environment:

.. code-block:: console
    
    $ conda create --yes -n {{cookiecutter.project_slug}} python=3.6
    $ conda activate {{cookiecutter.project_slug}}
    $ pip install -r requirements.txt
    $ make install


Now you can run

.. code-block:: console

    $ which {{cookiecutter.project_slug}}


and you should see `{{cookiecutter.project_slug}}` in your
environment's `bin/` directory.


Running {{cookiecutter.project_slug}}
--------{% for _ in cookiecutter.project_slug %}-{% endfor %}


.. code-block:: console

    $ {{cookiecutter.project_slug}} setup -n example
    $ cd example
    # Edit the config.yaml to your specific project needs
    $ {{cookiecutter.project_slug}} run config.yaml


Details
-------

The entrypoint of the command line interface is
the `main()` function of `{{ cookiecutter.project_slug }}/command.py`.

The location of the Snakefile is `{{ cookiecutter.project_slug }}/Snakefile`.
