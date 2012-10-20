import traceback
from flxinjection.domain import EntityFactory, EntityReference, Action
from flxinjection.libexceptions import BindingsInstantiationException, BindingsResolutionException, BindingsImportError
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
                raise BindingsImportError("no such factory for \"%s\"" % clazzpath)

            return clazz

        except ImportError, e:

            raise BindingsImportError("no such factory for \"%s\"" % entity.factory, e)

    def _init_factory(self, entity, clazz):
        """
        :type entity: flxinjection.domain.BaseEntity
        """
        try:
            parameters = self._resolve_parameters(entity)
            obj = clazz(**parameters)
            return obj

        except BindingsResolutionException, e:

            raise

        except Exception, e:

            print "e:", e
            print "*" * 80
            raise BindingsInstantiationException("exception while instantiating \"%s\"" % entity, e)

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
        try:
            if isinstance(factory, EntityFactory):
                return factory.build()

            if isinstance(factory, Action):
                return factory.run()

            return factory

        except Exception, e:

            raise BindingsInstantiationException("exception while building \"%s\"" % entity, e)
