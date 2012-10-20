"""
Unit-tests for the bindings configuration reader
"""
from nose.tools.nontrivial import raises
from flxbindings.libexceptions import BindingsConfigurationException
from flxbindings.logutil import dynamiclogger
from flxbindings.manager import BindingsManager

class TestConfiguration(object):
    """
    Unit-tests for the bindings configuration reader
    """
    _logger = dynamiclogger()

    def test_load_configuration(self):
        """
        Test loading a configuration file
        """
        manager = BindingsManager.load_from_filepath("/Users/aaron/IdeaProjects/flx-injection/tests/test_flxbindings/resources/test_configuration.yaml")

        properties1 = manager.resolve("properties-1")
        component1 = manager.resolve("component-1")
        action1 = manager.resolve("action-1")

        assert properties1 is not None
        assert component1 is not None
        assert action1 is not None

    def test_relative_child_configuration(self):
        """
        [Feature not implemented]
        """

    @raises(BindingsConfigurationException)
    def test_missing_filepath(self):
        """
        Test importing a config file that doesn't exist
        """
        BindingsManager.load_from_filepath("/tmp/foo.yaml")

    @raises(BindingsConfigurationException)
    def test_invalid_file(self):
        """
        Test importing a configuration file that isn't YAML
        """
        manager = BindingsManager.load_from_filepath("/Users/aaron/IdeaProjects/flx-injection/tests/test_flxbindings/resources/test_invalid_file.txt")

    def test_corrupt_file(self):
        """
        """
