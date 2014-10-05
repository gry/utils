__author__ = "Mario Rivas <h@cked.es>"
__version__ = "1.0"

from threadpool import ThreadPool

for c in locals().values():
    if issubclass(type(c), type) or type(c).__name__ == 'classobj':
        # classobj for exceptions :/
        c.__module__ = __name__
del c


__all__=['ThreadPool'] 
