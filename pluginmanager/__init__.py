__author__ = "Mario Rivas"
__version__ = "1.0"

from plugin_manager import PluginManager
import plugins

# fix module names for epydoc
for c in locals().values():
    if issubclass(type(c), type) or type(c).__name__ == 'classobj':
        # classobj for exceptions :/
        c.__module__ = __name__
del c


__all__=['PluginManager', 'plugins'] 

