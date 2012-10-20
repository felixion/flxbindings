"""
Unit-tests for various error cases related to entity resolution
"""
from nose.tools.nontrivial import raises
from flxbindings.domain import Component, EntityReference
from flxbindings.libexceptions import BindingsDependencyException, BindingsInstantiationException, BindingsResolutionException, BindingsImportError
from flxbindings.logutil import dynamiclogger
from flxbindings.manager import BindingsManager
from test_flxbindings.fixture.generics import InitExceptionFactory, InitException, BuildException

class TestEntityErrors(object):
    """
    Unit-tests for various error cases related to entity resolution
    """
    _logger = dynamiclogger()

    def setup(self):
        """
        Create new instance of BindingsManager for each test
        """
        self.manager = BindingsManager()

    @raises(BindingsImportError)
    def test_factory_missing_top_package(self):
        """
        Test resolving an entity whose top-level package doesn't exist
        """
        component = Component("component1", "foo.module.ComponentFactory")
        self.manager.add_entity(component)
        self.manager.resolve("component1")

    @raises(BindingsImportError)
    def test_factory_missing_last_module(self):
        """
        Test resolving an entity whose inner-most module doesn't exist
        """
        component = Component("component2", "test_flxbindings.fixture.foo.GenericFactory1")
        self.manager.add_entity(component)
        self.manager.resolve("component2")

    @raises(BindingsImportError)
    def test_factory_missing_class(self):
        """
        Test resolving an entity whose class doesn't exist
        """
        component = Component("component3", "test_flxbindings.fixture.generics.GenericFactoryFoo")
        self.manager.add_entity(component)
        self.manager.resolve("component3")

    @raises(BindingsInstantiationException)
    def test_exception_factory_init(self):
        """
        Test resolving an entity who throws an exception in __init__
        """
        component = Component("component4", "test_flxbindings.fixture.generics.InitExceptionFactory")
        self.manager.add_entity(component)
        self.manager.resolve("component4")

    @raises(BindingsInstantiationException)
    def test_exception_factory_build(self):
        """
        Test resolving an entity who throws an exception in build
        """
        component = Component("component5", "test_flxbindings.fixture.generics.BuildExceptionFactory")
        self.manager.add_entity(component)
        self.manager.resolve("component5")

    @raises(BindingsInstantiationException)
    def test_exception_action_init(self):
        """
        Test running an action who throws an exception in __init__
        """
        component = Component("component6", "test_flxbindings.fixture.generics.RunExceptionAction")
        self.manager.add_entity(component)
        self.manager.resolve("component6")

    @raises(BindingsInstantiationException)
    def test_exception_action_run(self):
        """
        Test running an action who throws an exception in run
        """
        component = Component("component7", "test_flxbindings.fixture.generics.InitExceptionAction")
        self.manager.add_entity(component)
        self.manager.resolve("component7")

    def test_exception_singleton(self):
        """
        Test resolving a singleton that throws an exception, multiple times
        """
        num_exceptions = InitExceptionFactory.NUM_EXCEPTIONS

        component = Component("component8", "test_flxbindings.fixture.generics.InitExceptionFactory")
        self.manager.add_entity(component)

        for _ in range(3):

            try:
                self.manager.resolve("component8")

            except BindingsInstantiationException, e:
                import traceback; traceback.print_exc()
                pass

        assert InitExceptionFactory.NUM_EXCEPTIONS == num_exceptions + 3, InitExceptionFactory.NUM_EXCEPTIONS

    @raises(BindingsResolutionException)
    def test_missing_parameter_reference(self):
        """
        Test resolving an entities whose parameter reference doesn't exist
        """
        component = Component("component9", "test_flxbindings.fixture.generics.GenericFactory1")
        component._parameters["param1"] = EntityReference("foo-entity")
        self.manager.add_entity(component)
        self.manager.resolve("component9")

    @raises(BindingsResolutionException)
    def test_missing_dependency_reference(self):
        """
        Test resolving an entity whose dependency doesn't exist
        """
        component = Component("component10", "test_flxbindings.fixture.generics.GenericFactory1")
        component._dependencies = [EntityReference("foo-entity")]
        self.manager.add_entity(component)
        self.manager.resolve("component10")
