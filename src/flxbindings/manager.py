import threading
from flxbindings.entbuilder import EntityBuilder
from flxbindings.entities import EntityConfigurationManager
from flxbindings.instancemgr import InstanceManager
from flxbindings.libexceptions import BindingsResolutionException
from flxbindings.logutil import dynamiclogger

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
        :type entity: flxbindings.domain.BaseEntity
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

        self.__lock = threading.Lock()
        self._instance = None

    def __get__(self, instance, owner):
        """"""
        if self._instance is None:
            try:
                self.__lock.acquire()

                if self._instance is None:
                    self._instance = self._manager.resolve(self._label)

            finally:
                self.__lock.release()

        return self._instance
