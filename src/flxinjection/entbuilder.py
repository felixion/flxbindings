import traceback
from flxinjection.domain import EntityFactory

class EntityBuilder(object):
    """
    """
    def build(self, label, entity):
        """
        :type entity: flxinjection.domain.BaseEntity
        """
        clazz = self._resolve_factory(entity)
        factory = self._init_factory(entity, clazz)
        obj = self._call_factory(entity, factory)
        return obj

    def _resolve_factory(self, entity):
        """
        :type entity: flxinjection.domain.BaseEntity
        """
        try:
            clazzpath = entity.factory
            modulename, clazzname = clazzpath.rsplit(".", 1)

            module = __import__(modulename, globals(), {}, [clazzname])
            clazz = getattr(module, clazzname, None)

            if not clazz:
                raise ImportError(clazzname)

            return clazz

        except ImportError, e:

            traceback.print_exc()

    def _init_factory(self, entity, clazz):
        """
        :type entity: flxinjection.domain.BaseEntity
        """
        parameters = entity._parameters
        obj = clazz(**parameters)
        return obj

    def _call_factory(self, entity, factory):
        """
        :type entity: flxinjection.domain.BaseEntity
        """
        if isinstance(factory, EntityFactory):
            return factory.build()

        return factory
