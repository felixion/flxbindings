from flxinjection.entbuilder import EntityBuilder
from flxinjection.entities import EntityConfigurationManager
from flxinjection.instancemgr import InstanceManager
from flxinjection.libexceptions import BindingsResolutionException
from flxinjection.logutil import dynamiclogger

class BindingsManager(object):
    """
    """
    _logger = dynamiclogger()

    def __init__(self):
        """
        """
        self._entities = EntityConfigurationManager()
        self._instances = InstanceManager(self)
        self._builder = EntityBuilder(self)

    def check(self, label):
        """
        Checks whether a label exists (without throwing an exception)
        """

    def resolve(self, label):
        """
        """
        self._logger.debug("resolve entity: %s" % label)

        entity_config = self._entities.resolve(label)

        if entity_config is None:
            raise BindingsResolutionException("no binding exists for label \"%s\"" % label)

        return self._instances.instantiate(label, entity_config, self._builder)

    def bind(self, label):
        """
        """
        self._logger.debug("creating dynamic binding for: %s" % label)
        return EntityBinding(self, label)

    def add_entity(self, entity):
        """
        :type entity: flxinjection.domain.BaseEntity
        """
        self._logger.debug("add entity: %s" % entity)
        self._entities.add_entity(entity)

class EntityBinding(object):
    """"""
    def __init__(self, manager, label):
        """
        :type manager: BindingsManager
        """
        self._manager = manager
        self._label = label

    def __get__(self, instance, owner):
        """"""
        return self._manager.resolve(self._label)
