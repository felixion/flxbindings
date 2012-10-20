class BindingsException(Exception):
    """
    """

class BindingsConfigurationException(BindingsException):
    """"""

class BindingsImportError(BindingsException):
    """
    """

class BindingsResolutionException(BindingsException):
    """"""

class BindingsInstantiationException(BindingsException):
    """"""

class BindingsDependencyException(BindingsInstantiationException):
    """"""
