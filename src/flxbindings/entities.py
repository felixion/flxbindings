from flxbindings.libexceptions import BindingsResolutionException

class EntityConfigurationManager(object):
    """
    """
    def __init__(self):
        """"""
        self._label_map = dict()
        self._factory_map = dict()
#        self._entity_configs = dict()

    def resolve(self, label):
        """
        """
        if label in self._label_map:
            return self._label_map[label]

        elif label in self._factory_map:
            return self._factory_map[label]

        else:
            raise BindingsResolutionException("no binding exists for label \"%s\"" % label)

    def add_entity(self, entity):
        """
        :type entity: flxbindings.domain.BaseEntity
        """
        self.__map_entity_label(entity)
        self.__map_entity_factory(entity)

    def __map_entity_label(self, entity):
        """
        :type entity: flxbindings.domain.BaseEntity
        """
        if entity.label:
            if entity.label in self._label_map:
                raise KeyError(entity.label) # TODO: message
            self._label_map[entity.label] = entity

    def __map_entity_factory(self, entity):
        """
        :type entity: flxbindings.domain.BaseEntity
        """
        if entity.factory in self._factory_map:
            return
        self._factory_map[entity.factory] = entity