"""
Module for reading bindings configurations from file
"""
from yaml.loader import Loader
from flxbindings.domain import EntityReference, Component, ActionEntity, Properties
from flxbindings.logutil import dynamiclogger

class ConfigurationLoader(Loader):
    """
    Customized YAML loader that can handle our tags.
    """
    _logger = dynamiclogger()

    def __init__(self, f):
        """"""
        super(ConfigurationLoader, self).__init__(f)
        self._setup_constructors()

    @classmethod
    def load_from_filepath(cls, filepath):
        """
        :rtype: list of BaseEntity
        """
        f = None
        try:
            f = open(filepath)
            loader = ConfigurationLoader(f)
            return loader.load()

        finally:
            if f: f.close()

    def load(self):
        """
        Reads the configuration from file
        :rtype: list of BaseEntity
        """
        return self.get_data()

    def _construct_configuration(self, loader, node):
        """
        :type loader: Loader
        """
        properties = loader.construct_sequence(node, deep = True)
        return properties

    def _construct_property(self, loader, node):
        """
        :type loader: Loader
        """
        properties = loader.construct_mapping(node, deep = True)
        label = properties.get("label", None)
        factory = properties["factory"]
        singleton = properties.get("singleton", False)
        parameters = properties.get("parameters", None)
        dependencies = properties.get("dependencies", None)

        props = Properties(label, factory, singleton, dependencies, parameters)
        return props

    def _construct_component(self, loader, node):
        """
        :type loader: Loader
        """
        properties = loader.construct_mapping(node, deep = True)
        label = properties.get("label", None)
        factory = properties["factory"]
        singleton = properties.get("singleton", False)
        parameters = properties.get("parameters", None)
        dependencies = properties.get("dependencies", None)

        component = Component(label, factory, singleton, dependencies, parameters)
        return component

    def _construct_reference(self, loader, tag, node):
        """
        :type loader: Loader
        """
        return EntityReference(tag)

    def _construct_action(self, loader, node):
        """
        :type loader: Loader
        """
        properties = loader.construct_mapping(node, deep = True)
        label = properties.get("label", None)
        factory = properties["factory"]
        singleton = properties.get("singleton", False)
        parameters = properties.get("parameters", None)
        dependencies = properties.get("dependencies", None)

        action = ActionEntity(label, factory, singleton, dependencies, parameters)
        return action

    def _setup_constructors(self):
        """"""
        self.add_constructor("!flxbindings/configuration", self._construct_configuration)
        self.add_constructor("!flxbindings/property", self._construct_property)
        self.add_constructor("!flxbindings/component", self._construct_component)
        self.add_multi_constructor("!flxbindings/reference:", self._construct_reference)
        self.add_constructor("!flxbindings/action", self._construct_action)

if __name__ == "__main__":

#    manager = BindingsManager()
#
#    filepath = "/Users/aaron/IdeaProjects/flx-injection/tests/test_flxbindings/resources/test_configuration.yaml"
#    data = ConfigurationLoader.load_from_filepath(filepath)
#
#    for d in data:
#        print "d:", d
#        if d._dependencies:
#            print "\tdependencies:", d._dependencies
#        if d._parameters:
#            print "\tparameters:", d._parameters
#
#        print
#
#        manager.add_entity(d)
#
#    import sys
#    sys.stdout.flush()
#    try:
#        print "props-1:", manager.resolve("properties-1")
#        print "comp-1:", manager.resolve("component-1")
#
#    except:
#        import traceback
#        traceback.print_exc()

    pass