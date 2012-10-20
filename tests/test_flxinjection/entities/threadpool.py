class ThreadPoolFactory(object):
    """
    """
    def __init__(self, size, logprops):
        """"""
        print "ThreadPoolFactory.init(size=%s, props=%s)" % (size, logprops)
        self._size = size
        self._logprops = logprops

    def run(self):
        """"""
