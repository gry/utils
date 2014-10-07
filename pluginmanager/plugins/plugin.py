"""
Base plugin
"""
class Plugin(object):
    """Base Plugin class"""

    name = "Base Plugin"
    category = "default"

    def __init__(self, *args, **kwargs):
        super(Plugin, self).__init__()
        self.args = args
        self.kwargs = kwargs

    """run is the only method a plugin must implement
    To create your own plugins, copy this class, change the parameters
    and define run
    """
    def run(self, *args, **kwargs):
        raise NotImplementedError("Plugin not implemented")
        
