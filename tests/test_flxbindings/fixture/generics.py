from flxinjection.domain import EntityFactory, Action

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

class InitException(Exception):
    """"""

class InitExceptionFactory(EntityFactory):
    """"""
    NUM_EXCEPTIONS = 0

    def __init__(self):
        """"""
        self.inc_exceptions()
        raise InitException("InitExceptionFactory")

    def build(self):
        """"""

    @classmethod
    def inc_exceptions(cls):
        """"""
        cls.NUM_EXCEPTIONS += 1

class BuildException(Exception):
    """"""

class BuildExceptionFactory(EntityFactory):
    """"""
    def __init__(self):
        """"""
        self._is_built = False

    def build(self):
        """"""
        raise BuildException("BuildExceptionFactory")

class InitException(Exception):
    """"""

class InitExceptionAction(Action):
    def run(self):
        """"""
        raise InitException("InitExceptionAction")

class RunException(Exception):
    """"""

class RunExceptionAction(Action):
    def run(self):
        """"""
        raise RunException("RunExceptionAction")