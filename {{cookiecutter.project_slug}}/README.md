# {{cookiecutter.project_slug}} snakemake-cli

[![travis](https://img.shields.io/travis/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}.svg)](https://travis-ci.org/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}})
[![license](https://img.shields.io/github/license/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}.svg)](https://github.com/sschmeier/{{cookiecutter.project_slug}}/blob/master/LICENSE)

An Snakemake command line interface
bundled up as an installable Python package.

This example bundles the Snakefile with the
command line tool, but this tool can also look
in the user's working directory for Snakefiles.

Snakemake functionality is provided through
a command line tool called `{{cookiecutter.project_slug}}`.

# Quickstart

This runs through the installation and usage
of `snakemake-cli`.

## Installing {{cookiecutter.project_slug}}

Start by setting up a conda environment,
and install the required packages into the
environment:

```bash
conda create --yes -n {{cookiecutter.project_slug}} python=3.6
conda activate {{cookiecutter.project_slug}}
pip install -r requirements.txt
```

Now install the `{{cookiecutter.project_slug}}` command line tool:

```bash
python setup.py build install
```

Now you can run

```bash
which {{cookiecutter.project_slug}}
```

and you should see `{{cookiecutter.project_slug}}` in your
environment's `bin/` directory.


## Running {{cookiecutter.project_slug}}

```bash
{{cookiecutter.project_slug}} setup
cd example
# edit config.yaml
{{cookiecutter.project_slug}} run config.yaml
```

# Details

The entrypoint of the command line interface is
the `main()` function of `cli/command.py`.

The location of the Snakefile is `cli/Snakefile`.
