from setuptools import setup, find_packages
import glob
import os

with open("requirements.txt") as f:
    required = [x for x in f.read().splitlines() if not x.startswith("#")]

# Note: the __program__ variable is set in __init__.py.
# it determines the name of the package/final command line tool.
from cli import __version__, __program__, __author__, __email__, __license__, __url__

setup(
    name=__program__,
    version=__version__,
    packages=["cli"],
    test_suite="pytest.collector",
    tests_require=["pytest"],
    description=__program__,
    url=__url__,
    author=__author__,
    author_email=__email__,
    license=__license__,
    entry_points="""
      [console_scripts]
      {program} = cli.command:main
      """.format(
        program=__program__
    ),
    install_requires=required,
    include_package_data=True,
    keywords=[],
    zip_safe=False,
)
