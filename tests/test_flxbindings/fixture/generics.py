from flxinjection.domain import EntityFactory

class GenericFactory1(EntityFactory):
    """"""
    RESULT = "GenericFactory1-Result"

    def __init__(self):
        """"""
        self._is_built = False

    def build(self):
        """"""
        self._is_built = True
        return self.RESULT

class GenericFactory2(EntityFactory):
    """"""
    def __init__(self):
        """"""
        self._is_built = False

    def build(self):
        """"""
        self._is_built = True

class InitExceptionFactory(EntityFactory):
    """"""
    def __init__(self):
        """"""
        raise Exception("InitExceptionFactory")

    def build(self):
        """"""

class BuildExceptionFactory(EntityFactory):
    """"""
    def __init__(self):
        """"""
        self._is_built = False

    def build(self):
        """"""
        raise Exception("BuildExceptionFactory")

