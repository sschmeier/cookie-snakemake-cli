.. highlight:: shell

============
Installation
============

1. Install conda
----------------

On Linux::

    $ curl -O https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
    $ bash Miniconda3-latest-Linux-x86_64.sh


On MacOS::

    $ curl -O https://repo.continuum.io/miniconda/Miniconda3-latest-MacOSX-x86_64.sh
    $ bash Miniconda3-latest-MacOSX-x86_64.sh



Add conda dir to PATH::

    $ echo 'export PATH="~/miniconda3/bin:$PATH"' >> ~/.bashrc
    $ echo 'export PATH="~/miniconda3/bin:$PATH"' >> ~/.zshrc


2. Install from source
----------------------

The sources for {{ cookiecutter.project_name }} can be downloaded from the `Github repo`_.

You can either clone the public repository:

.. code-block:: console

    $ git clone git://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}

Or download the `tarball`_:

.. code-block:: console

    $ curl -OJL https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/tarball/master

Once you have a copy of the source, you can install it with:

.. code-block:: console

    $ conda create --yes -n {{cookiecutter.project_slug}} python=3.6
    $ conda activate {{cookiecutter.project_slug}}
    $ pip install -r requirements.txt
    $ make install


.. _Github repo: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}
.. _tarball: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/tarball/master
