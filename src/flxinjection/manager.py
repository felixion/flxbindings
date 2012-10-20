from flxinjection.entbuilder import EntityBuilder
from flxinjection.entities import EntityConfigurationManager
from flxinjection.instancemgr import InstanceManager
from flxinjection.logutil import dynamiclogger

class BindingsManager(object):
    """
    """
    _logger = dynamiclogger()

    def __init__(self):
        """
        """
        self._entities = EntityConfigurationManager()
        self._instances = InstanceManager()
        self._builder = EntityBuilder()

    def resolve(self, label):
        """
        """
        self._logger.debug("resolve entity: %s" % label)

        entity_config = self._entities.resolve(label)

        if entity_config is None:
            raise KeyError(label) # TODO: message

        return self._instances.instantiate(label, entity_config, self._builder)

    def add_entity(self, entity):
        """
        :type entity: flxinjection.domain.BaseEntity
        """
        self._logger.debug("add entity: %s" % entity)
        self._entities.add_entity(entity)
