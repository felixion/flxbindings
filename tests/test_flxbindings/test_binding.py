"""
Unit-tests for the attribute binding mechanism
"""
from flxbindings.domain import Component
from flxbindings.logutil import dynamiclogger
from flxbindings.manager import BindingsManager
from test_flxbindings.fixture.generics import GenericFactory1

manager = BindingsManager()

component1 = Component("component1", "test_flxbindings.fixture.generics.GenericFactory1")
component1._singleton = False
component2 = Component("component2", "test_flxbindings.fixture.generics.GenericFactory2")
component2._singleton = False

manager.add_entity(component1)
manager.add_entity(component2)

class ExampleClient1(object):
    """
    Example class with bound attributes
    """
    binding1 = manager.bind("component1")
    binding2 = manager.bind("component2")

    def test_referencing_binding(self):
        """"""
        for _ in range(3):
            print self.binding1

class ExampleClient2(object):
    """
    Example class with bound attributes
    """
    binding1 = manager.bind("component1")
    binding2 = manager.bind("component2")

    def test_referencing_binding(self):
        """"""
        for _ in range(3):
            print self.binding1

class TestBinding(object):
    """
    Unit-tests for the attribute binding mechanism
    """
    _logger = dynamiclogger()

    def test_rereferencing_binding(self):
        """
        Test dynamically binding components to object properties
        """
        num_inits = GenericFactory1.NUM_INITS

        client1 = ExampleClient1()
        client1.test_referencing_binding()

        assert GenericFactory1.NUM_INITS == num_inits + 1, GenericFactory1.NUM_INITS

        client2 = ExampleClient2()
        client2.test_referencing_binding()

        assert GenericFactory1.NUM_INITS == num_inits + 2, GenericFactory1.NUM_INITS
