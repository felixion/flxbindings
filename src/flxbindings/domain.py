class BaseEntity(object):
    """
    """
    def __init__(self, label = None, factory = None, singleton = True, dependencies = None, parameters = None):
        """
        """
        self._label = label
        self._factory = factory
        self._singleton = singleton
        self._dependencies = dependencies or list()
        self._parameters = parameters or dict()

    @property
    def label(self):
        """"""
        return self._label

    @property
    def factory(self):
        """"""
        return self._factory

    @property
    def singleton(self):
        """"""
        return self._singleton

    def __repr__(self):
        """"""
        return "#<%s :label %s :factory %s>" % (self.__class__.__name__, self.label, self.factory)

class Component(BaseEntity):
    """"""

class Properties(BaseEntity):
    """"""

class ActionEntity(BaseEntity):
    """"""

class EntityReference(object):
    """"""
    def __init__(self, label):
        """"""
        self._label = label

    @property
    def label(self):
        """"""
        return self._label

class EntityFactory(object):
    """"""
    def build(self):
        """"""
        raise NotImplementedError()

class Action(object):
    """"""
    def run(self):
        """"""
        return NotImplemented
