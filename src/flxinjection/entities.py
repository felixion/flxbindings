class EntityConfigurationManager(object):
    """
    """
    def __init__(self):
        """"""
        self._entity_configs = dict()

    def resolve(self, label):
        """
        """
        return self._entity_configs.get(label, None)

    def add_entity(self, entity):
        """
        :type entity: flxinjection.domain.BaseEntity
        """
        label = entity.label

        if label in self._entity_configs:
            raise KeyError(label) # TODO: message

        self._entity_configs[label] = entity
