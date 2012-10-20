"""
Unit-tests to ensure singletons are handled correctly
"""
from flxbindings.domain import Component, EntityReference
from flxbindings.logutil import dynamiclogger
from flxbindings.manager import BindingsManager
from test_flxbindings.fixture.generics import GenericFactory1, GenericFactory2

class TestSingletonHandling(object):
    """
    Unit-tests to ensure singletons are handled correctly
    """
    _logger = dynamiclogger()

    def setup(self):
        """
        Create new instance of BindingsManager for each test
        """
        self.manager = BindingsManager()

    def test_singleton(self):
        """
        Ensure singletons only created once
        """
        num_inits = GenericFactory1.NUM_INITS

        component = Component("component1", "test_flxbindings.fixture.generics.GenericFactory1")
        self.manager.add_entity(component)

        self.manager.resolve("component1")
        self.manager.resolve("component1")
        self.manager.resolve("component1")

        assert GenericFactory1.NUM_INITS == num_inits + 1, GenericFactory1.NUM_INITS

    def test_non_singleton(self):
        """
        Ensure non-singletons created every time
        """
        num_inits = GenericFactory1.NUM_INITS

        component = Component("component2", "test_flxbindings.fixture.generics.GenericFactory1")
        component._singleton = False
        self.manager.add_entity(component)

        self.manager.resolve("component2")
        self.manager.resolve("component2")
        self.manager.resolve("component2")

        assert GenericFactory1.NUM_INITS == num_inits + 3, GenericFactory1.NUM_INITS

    def test_reference_singleton(self):
        """
        Ensure a referenced singleton only created once
        """
        num_inits1 = GenericFactory1.NUM_INITS
        num_inits2 = GenericFactory2.NUM_INITS

        component3_1 = Component("component3_1", "test_flxbindings.fixture.generics.GenericFactory1")
        component3_1._singleton = False
        component3_1._parameters["param1"] = EntityReference("component3_2")
        component3_2 = Component("component3_2", "test_flxbindings.fixture.generics.GenericFactory2")

        self.manager.add_entity(component3_1)
        self.manager.add_entity(component3_2)

        self.manager.resolve("component3_1")
        self.manager.resolve("component3_1")
        self.manager.resolve("component3_1")

        assert GenericFactory1.NUM_INITS == num_inits1 + 3, GenericFactory1.NUM_INITS
        assert GenericFactory2.NUM_INITS == num_inits2 + 1, GenericFactory2.NUM_INITS

    def test_owner_singleton(self):
        """
        Ensure a singleton owners' non-singleton dependencies not recreatred
        """
        num_inits1 = GenericFactory1.NUM_INITS
        num_inits2 = GenericFactory2.NUM_INITS

        component4_1 = Component("component4_1", "test_flxbindings.fixture.generics.GenericFactory1")
        component4_1._parameters["param1"] = EntityReference("component4_2")
        component4_2 = Component("component4_2", "test_flxbindings.fixture.generics.GenericFactory2")
        component4_2._singleton = False

        self.manager.add_entity(component4_1)
        self.manager.add_entity(component4_2)

        self.manager.resolve("component4_1")
        self.manager.resolve("component4_1")
        self.manager.resolve("component4_1")

        assert GenericFactory1.NUM_INITS == num_inits1 + 1, GenericFactory1.NUM_INITS
        assert GenericFactory2.NUM_INITS == num_inits2 + 1, GenericFactory2.NUM_INITS

    def test_non_singleton_dependency(self):
        """
        Ensure non-singleton dependencies are executed every time
        """
        num_inits1 = GenericFactory1.NUM_INITS
        num_inits2 = GenericFactory2.NUM_INITS

        component5_1 = Component("component5_1", "test_flxbindings.fixture.generics.GenericFactory1")
        component5_1._singleton = False
        component5_2 = Component("component5_2", "test_flxbindings.fixture.generics.GenericFactory2")
        component5_2._dependencies = [component5_1]

        self.manager.add_entity(component5_1)
        self.manager.add_entity(component5_2)

        self.manager.resolve("component5_2")
        self.manager.resolve("component5_2")
        self.manager.resolve("component5_2")

        assert GenericFactory1.NUM_INITS == num_inits1 + 1, GenericFactory1.NUM_INITS
        assert GenericFactory2.NUM_INITS == num_inits2 + 1, GenericFactory2.NUM_INITS

    def test_singleton_dependency(self):
        """
        Ensure singleton dependencies are not executed twice
        """
        num_inits1 = GenericFactory1.NUM_INITS
        num_inits2 = GenericFactory2.NUM_INITS

        component5_1 = Component("component5_1", "test_flxbindings.fixture.generics.GenericFactory1")
        component5_2 = Component("component5_2", "test_flxbindings.fixture.generics.GenericFactory2")
        component5_2._dependencies = [component5_1]
        component5_2._singleton = False

        self.manager.add_entity(component5_1)
        self.manager.add_entity(component5_2)

        self.manager.resolve("component5_2")
        self.manager.resolve("component5_2")
        self.manager.resolve("component5_2")

        assert GenericFactory1.NUM_INITS == num_inits1 + 1, GenericFactory1.NUM_INITS
        assert GenericFactory2.NUM_INITS == num_inits2 + 3, GenericFactory2.NUM_INITS

    def test_singleton_parameter_reference(self):
        """
        [Covered by test_reference_singleton?]
        Ensure singleton parameters are not executed twice
        """

    def test_non_singleton_parameter_reference(self):
        """
        Ensure non-singleton parameters are executed every time
        """
        num_inits1 = GenericFactory1.NUM_INITS
        num_inits2 = GenericFactory2.NUM_INITS

        component3_1 = Component("component3_1", "test_flxbindings.fixture.generics.GenericFactory1")
        component3_1._parameters["param1"] = EntityReference("component3_2")
        component3_2 = Component("component3_2", "test_flxbindings.fixture.generics.GenericFactory2")
        component3_2._singleton = False

        self.manager.add_entity(component3_1)
        self.manager.add_entity(component3_2)

        self.manager.resolve("component3_1")
        self.manager.resolve("component3_1")
        self.manager.resolve("component3_1")

        assert GenericFactory1.NUM_INITS == num_inits1 + 1, GenericFactory1.NUM_INITS
        assert GenericFactory2.NUM_INITS == num_inits2 + 1, GenericFactory2.NUM_INITS
