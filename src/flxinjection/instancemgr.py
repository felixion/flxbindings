class InstanceManager(object):
    """
    """
    def __init__(self):
        """"""
        self._instances = dict()
    
    def instantiate(self, label, entity, builder):
        """
        :type entity: flxinjection.domain.BaseEntity
        :type builder: flxinjection.entbuilder.EntityBuilder
        """

        # if not singleton, build new object
        if not entity.singleton:
            return self._create_entity(label, entity, builder)
        
        # determine if singleton object already built...
        if self._has_instance(label, entity):
            return self._resolve_instance(label, entity)
        
        # build object and store singleton
        return self._build_singleton(label, entity, builder)

    def _create_entity(self, label, entity, builder):
        """
        :type entity: flxinjection.domain.BaseEntity
        :type builder: flxinjection.entbuilder.EntityBuilder
        """
        return builder.build(label, entity)

    def _has_instance(self, label, entity):
        """
        :type entity: flxinjection.domain.BaseEntity
        :type builder: flxinjection.entbuilder.EntityBuilder
        """
        return label in self._instances

    def _resolve_instance(self, label, entity):
        """
        :type entity: flxinjection.domain.BaseEntity
        :type builder: flxinjection.entbuilder.EntityBuilder
        """
        return self._instances.get(label, None)

    def _build_singleton(self, label, entity, builder):
        """
        :type entity: flxinjection.domain.BaseEntity
        :type builder: flxinjection.entbuilder.EntityBuilder
        """
        obj = self._create_entity(label, entity, builder)
        self._instances[label] = obj
        return obj
