from flxbindings.domain import EntityFactory, Action

class BaseFactory(EntityFactory):
    NUM_INITS = 0
    NUM_BUILDS = 0

    def __init__(self):
        """"""
        self.inc_init()

    def build(self):
        """"""
        self.inc_build()

    @classmethod
    def inc_init(cls):
        """"""
        cls.NUM_INITS += 1

    @classmethod
    def inc_build(cls):
        """"""
        cls.NUM_BUILDS += 1

class GenericFactory1(BaseFactory):
    """"""
    RESULT = "GenericFactory1-Result"

    def __init__(self, **kwargs):
        """"""
        super(GenericFactory1, self).__init__()
        self._is_built = False

    def build(self):
        """"""
        super(GenericFactory1, self).build()
        self._is_built = True
        return self.RESULT

class GenericFactory2(BaseFactory):
    """"""
    def __init__(self, **kwargs):
        """"""
        super(GenericFactory2, self).__init__()
        self._is_built = False

    def build(self):
        """"""
        super(GenericFactory2, self).build()
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