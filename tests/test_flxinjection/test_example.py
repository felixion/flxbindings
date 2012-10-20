import logging
import sys

from flxinjection.domain import Component, Properties, EntityReference
from flxinjection.logutil import dynamiclogger
from flxinjection.manager import BindingsManager

manager = BindingsManager()

class ExampleClient(object):

    component1 = manager.bind("logging-properties")

    def run(self):
        """"""
        print "ExampleClient.run"
        print self.component1

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

        cls._create_config_objects()

    def setup(self):
        """"""
        print "setup"


    def __init__(self):
        """"""
#        self._manager = BindingsManager()

    def test_1(self):
        """"""
        self._logger.debug("instantiating threadpool")

        threadpool = self._instantiate()
        print "threadpool:", threadpool

        threadpool = self._instantiate()
        print "threadpool:", threadpool

    def _instantiate(self):
        """"""
        return manager.resolve("threadpool")

    def test_2(self):

        logging_properties = manager.resolve("logging-properties")
        print "props:", logging_properties

    def test_3(self):

        client = ExampleClient()
        client.run()

    @classmethod
    def _create_config_objects(cls):
        """"""
        threadpool = Component()
        threadpool._label = "threadpool"
        threadpool._factory = "test_flxinjection.entities.threadpool.ThreadPoolFactory"
        threadpool._parameters["size"] = 10
        threadpool._parameters["logprops"] = EntityReference("logging-properties")

        props = Properties()
        props._label = "logging-properties"
        props._factory = "test_flxinjection.entities.logents.LoggingPropertiesFactory"
        props._parameters["filepath"] = "foo.yaml"

        manager.add_entity(threadpool)
        manager.add_entity(props)
