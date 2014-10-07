from plugin import Plugin

class ExamplePlugin(Plugin):
    """Example Plugin"""

    name = "Example"
    category = "example"
    description = "Example plugin"

    def __init__(self, *args, **kwargs):
        super(ExamplePlugin, self).__init__()
        self.args = args
        self.kwargs = kwargs

    def run(self, url, method,*args, **kwargs):
        print "Executing %s" %self.__name__()
        print url, method
        print self.args
        print args
        print kwargs
        
