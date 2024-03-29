from flxbindings.libexceptions import BindingsInstantiationException, BindingsException
from flxbindings.logutil import dynamiclogger

class InstanceManager(object):
    """
    """
    _logger = dynamiclogger()

    def __init__(self, manager):
        """
        :type manager: flxbindings.manager.BindingsManager
        """
        self._manager = manager
        self._instances = dict()
    
    def instantiate(self, label, entity, builder):
        """
        :type entity: flxbindings.domain.BaseEntity
        :type builder: flxbindings.entbuilder.EntityBuilder
        """
        try:
            # determine if singleton object already built...
            if entity.singleton and self._has_instance(label, entity):
                return self._resolve_instance(label, entity)

            # handle dependencies
            self._instantiate_dependencies(label, entity, builder)

            # if not singleton, build new object
            if not entity.singleton:
                return self._create_entity(label, entity, builder)

            # build object and store singleton
            return self._build_singleton(label, entity, builder)

        except BindingsException, e:

            raise e

        except Exception, e:

            raise BindingsInstantiationException("exception instantiating entity %s" % entity, e)

    def _create_entity(self, label, entity, builder):
        """
        :type entity: flxbindings.domain.BaseEntity
        :type builder: flxbindings.entbuilder.EntityBuilder
        """
        return builder.build(label, entity)

    def _has_instance(self, label, entity):
        """
        :type entity: flxbindings.domain.BaseEntity
        :type builder: flxbindings.entbuilder.EntityBuilder
        """
        return label in self._instances

    def _resolve_instance(self, label, entity):
        """
        :type entity: flxbindings.domain.BaseEntity
        :type builder: flxbindings.entbuilder.EntityBuilder
        """
        return self._instances.get(label, None)

    def _build_singleton(self, label, entity, builder):
        """
        :type entity: flxbindings.domain.BaseEntity
        :type builder: flxbindings.entbuilder.EntityBuilder
        """
        obj = self._create_entity(label, entity, builder)
        self._instances[label] = obj
        return obj

    def _instantiate_dependencies(self, label, entity, builder):
        """
        :type entity: flxbindings.domain.BaseEntity
        :type builder: flxbindings.entbuilder.EntityBuilder
        """
        for dependency in entity._dependencies:
            self._logger.debug("instantiate dependency: %s" % dependency)
            self._manager.resolve(dependency.label)
