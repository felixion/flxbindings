"""
Unit-tests for resolving entities
"""
from nose.tools.nontrivial import raises

from flxbindings.logutil import dynamiclogger
from flxbindings.manager import BindingsManager

from test_flxbindings.fixture import entity_resolution
from test_flxbindings.fixture.generics import GenericFactory1

class TestEntityResolution(object):
    """
    Unit-tests for resolving entities
    """
    _logger = dynamiclogger()

    def setup(self):
        """
        Create new instance of BindingsManager for each test
        """
        self.manager = BindingsManager()

    def test_resolve_label(self):
        """
        An entity can be resolved by its label
        """
        entities = [entity_resolution.component1]
        self.__import_entities(entities)

        instance = self.manager.resolve("component1")
        assert instance == GenericFactory1.RESULT

    def test_resolve_instance(self):
        """
        [Not implemented] resolving entities using their instance
        """

    def test_resolve_factory(self):
        """
        An entity can be resolved by its factory
        """
        entities = [entity_resolution.component1]
        self.__import_entities(entities)

        instance = self.manager.resolve("test_flxbindings.fixture.generics.GenericFactory1")
        assert instance == GenericFactory1.RESULT

    def test_no_label_entity(self):
        """
        An entity with factory (but not label) can be resolved
        """
        entities = [entity_resolution.component4]
        self.__import_entities(entities)

        instance = self.manager.resolve("test_flxbindings.fixture.generics.GenericFactory1")
        assert instance == GenericFactory1.RESULT

    def test_no_interface_entity(self):
        """
        [Not implemented] resolving entities with no instance defined
        """

    def test_factory_only_entity(self):
        """
        [NA] convered by test_no_label_entity until interfaces implemented
        """

    @raises(KeyError)
    def test_duplicate_label_mapping(self):
        """
        Ensure there is an error when attempting to map more than one entity
        with the same label.
        """
        entities = [entity_resolution.component5_1, entity_resolution.component5_2]
        self.__import_entities(entities)

        instance = self.manager.resolve("foo5")
        assert instance == GenericFactory1.RESULT

    def test_share_interface_mapping(self):
        """
        [Not implemented] multiple entities with the same interface
        """

    def test_share_factory_mapping(self):
        """
        Ensure that duplicate factories can exist.
        """
        entities = [entity_resolution.component6_1, entity_resolution.component6_2]
        self.__import_entities(entities)

        instance = self.manager.resolve("test_flxbindings.fixture.generics.GenericFactory1")
        assert instance == GenericFactory1.RESULT

    def test_lookup_duplicate_interface(self):
        """
        [Not implemented] duplicate of test_share_interface_mapping?
        """

    def test_lookup_duplicate_factory(self):
        """
        Can resolve entities based on factories even if multiple exist
        """
        entities = [entity_resolution.component8_1, entity_resolution.component8_2]
        self.__import_entities(entities)

        instance = self.manager.resolve("test_flxbindings.fixture.generics.GenericFactory1")
        assert instance == GenericFactory1.RESULT

    def __import_entities(self, entities):
        """
        Imports a sequence of entities into the BindingsManager
        :param entities: list of BaseEntity
        """
        for entity in entities:
            self._logger.info("adding entity: %s" % entity)
            self.manager.add_entity(entity)
