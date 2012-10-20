from flxinjection.domain import EntityFactory
import logging

class LoggingProperties(object):
    """"""
    def __init__(self):
        """"""
        print "LoggingProperties.__init__()"
        self._level = logging.INFO
        self._logfile = "debug.log"

class LoggingPropertiesFactory(EntityFactory):
    """"""
    def __init__(self, filepath):
        """"""
        self._filepath = filepath

    def build(self):
        """"""
        return LoggingProperties()
