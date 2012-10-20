import traceback
from flxinjection.domain import EntityFactory, EntityReference
from flxinjection.logutil import dynamiclogger

class EntityBuilder(object):
    """
    """
    _logger = dynamiclogger()

    def __init__(self, manager):
        """
        :type manager: flxinjection.manager.BindingsManager
        """
        self._manager = manager

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
        parameters = self._resolve_parameters(entity)
        obj = clazz(**parameters)
        return obj

    def _resolve_parameters(self, entity):
        """"""
        def _resolve_parameter(param, value):
            if isinstance(value, EntityReference):

                reference_label = value._label
                self._logger.debug("dynamically resolving parameter: %s" % reference_label)
                newvalue = self._manager.resolve(reference_label)
                return param, newvalue

            return param, value

        return dict([_resolve_parameter(param, value) for param, value in entity._parameters.iteritems()])

    def _call_factory(self, entity, factory):
        """
        :type entity: flxinjection.domain.BaseEntity
        """
        if isinstance(factory, EntityFactory):
            return factory.build()

        return factory
