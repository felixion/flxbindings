class BaseEntity(object):
    """
    """
    def __init__(self):
        """
        """
        self._label = None
        self._factory = None
        self._singleton = True
        self._dependencies = list()
        self._parameters = dict()

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
        return "#<BaseEntity :label %s :factory %s>" % (self.label, self.factory)

class Component(BaseEntity):
    """"""

class Properties(BaseEntity):
    """"""

class EntityFactory(object):
    """"""
    def build(self):
        """"""
        raise NotImplementedError()
