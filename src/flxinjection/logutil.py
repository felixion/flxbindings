from weakref import WeakKeyDictionary
import logging

class dynamiclogger(object):

    def __init__(self):
        """"""
        self._instance = None

    def __get__(self, instance, owner):
        """
        :rtype: logging.Logger
        """
        if self._instance is None:
            clazzname = owner.__name__
            self._instance = logging.getLogger(clazzname)
        return self._instance
