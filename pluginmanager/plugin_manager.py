#!/usr/bin/env python
import sys

class PluginManager():
    
    
    def getPlugins(self, categories = None):
    """Returns the plugin_list of all plugins of the given categories,
    or all the plugins if categories is not specified
    Returns: List[Subclass<Plugin>]
    Params:
        categories: List[String]
    """
        import plugins
        from plugins.plugin import Plugin
        if categories is None or len(categories) == 0:
            plugin_list = Plugin.__subclasses__()
        else:
            plugin_list = [p for p in Plugin.__subclasses__() if p.category in categories]
        return plugin_list

def main():
    sys.argv.pop(0)
    print PluginManager().getPlugins(sys.argv)

if __name__ == '__main__':
    main()
