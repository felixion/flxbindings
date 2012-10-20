import logging
import sys

from flxinjection.domain import Component, Properties
from flxinjection.logutil import dynamiclogger
from flxinjection.manager import BindingsManager

class TestExample(object):

    _logger = dynamiclogger()

    @classmethod
    def setup_class(cls):
        """"""
        logger = logging.getLogger("")
        logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter("[%(asctime)s] %(msg)s")

        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(formatter)

        logger.addHandler(handler)

    def setup(self):
        """"""
        print "setup"
        self._create_config_objects()

    def __init__(self):
        """"""
        self._manager = BindingsManager()

    def test_1(self):
        """"""
        self._logger.debug("instantiating threadpool")

        threadpool = self._instantiate()
        print "threadpool:", threadpool

        threadpool = self._instantiate()
        print "threadpool:", threadpool

    def _instantiate(self):
        """"""
        return self._manager.resolve("threadpool")

    def test_2(self):

        logging_properties = self._manager.resolve("logging-properties")
        print "props:", logging_properties

    def _create_config_objects(self):
        """"""
        threadpool = Component()
        threadpool._label = "threadpool"
        threadpool._factory = "test_flxinjection.entities.threadpool.ThreadPoolFactory"
        threadpool._parameters["size"] = 10

        props = Properties()
        props._label = "logging-properties"
        props._factory = "test_flxinjection.entities.logging.LoggingPropertiesFactory"
        props._parameters["filepath"] = "foo.yaml"

        self._manager.add_entity(threadpool)
        self._manager.add_entity(props)
