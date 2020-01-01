import pytest
from subprocess import call, Popen, PIPE
import os


"""
test {{cookiecutter.project_slug}}

this test will run {{cookiecutter.project_slug}} with the test
config and params provided in the test dir.

this test will also show how to run tests where
failure is expected (i.e., checking that we handle
invalid parameters).

each test has a unittest TestCase defined.
pytest will automatically find these tests.
"""


class Test:
    """
    simple {{cookiecutter.project_slug}} test class

    This uses the subprocess PIPE var
    to capture system input and output,
    since we are running {{cookiecutter.project_slug}} from the
    command line directly using subprocess.
    """

    @classmethod
    def setUpClass(self):
        """
        set up a {{cookiecutter.project_slug}} workflow test.

        we are using the existing tests/ dir
        as our working dir, so no setup to do.

        if we were expecting the user to provide
        a Snakefile, this is where we would set
        up a test Snakefile.
        """
        pass

    def test_setup(self):
        """
        test workflow
        """
        command = ["{{ cookiecutter.project_slug }}", "setup", "-n", "test"]
        pwd = os.path.abspath(os.path.dirname(__file__))
        child = Popen(command, cwd=pwd, stdout=PIPE)
        streamdata = child.communicate()[0]
        rc = child.returncode
        assert rc == 0

    def test_run(self):
        """
        test workflow
        """
        command_prefix = ["{{ cookiecutter.project_slug }}", "run"]

        params = ["test/config.yaml"]

        pwd = os.path.abspath(os.path.dirname(__file__))

        for param in params:

            command = command_prefix + [param]

            child = Popen(command, cwd=pwd, stdout=PIPE)
            streamdata = child.communicate()[0]
            rc = child.returncode
            assert rc == 0

            # clean up
            call(["rm", "-rf", "analysis"])

    @classmethod
    def tearDownClass(self):
        """
        clean up after the tests
        """
        pass
