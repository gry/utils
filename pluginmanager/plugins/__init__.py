from glob import glob
from keyword import iskeyword
from os.path import dirname, join, split, splitext

# Got this __init__ from: https://github.com/samwyse/sspp

basedir = dirname(__file__)

__all__ = []
for name in glob(join(basedir, '*.py')):
    module = splitext(split(name)[-1])[0]
    if not module.startswith('_') and not iskeyword(module):
        try:
            __import__(__name__+'.'+module)
        except:
            print __name__+'.'+module
            import logging
            logger = logging.getLogger(__name__)
            logger.warning('Ignoring exception while loading the %r plug-in.', module)
        else:
            __all__.append(module)
__all__.sort()
