class BindingsException(Exception):
    """
    """

class BindingsImportError(BindingsException):
    """
    """

class BindingsResolutionException(BindingsException):
    """"""

class BindingsInstantiationException(BindingsException):
    """"""

class BindingsDependencyException(BindingsInstantiationException):
    """"""
