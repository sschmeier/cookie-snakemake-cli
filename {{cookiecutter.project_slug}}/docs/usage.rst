=====
Usage
=====

1. Setup an example directory with files needed for the project::

    $ {{cookiecutter.project_slug}} setup -n example


2. Enter the directory::

    $ cd example

    Edit the config.yaml to your specific project needs

    
3. Run the Snakemake workflow::

    $ {{cookiecutter.project_slug}} run config.yaml
