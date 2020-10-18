class Singleton(object):
    '''
    Guido's singleton implementation.  Use as a class base whenever Singleton
    behavior is desired for a class.  Override `init()` to initialize the
    instance; `__init__` is called every time the constructor is invoked
    and may not be desirable for a true singleton.
    '''

    def __new__(cls, *args, **kwds):
        it = cls.__dict__.get("__it__")
        if it is not None:
            return it
        cls.__it__ = it = object.__new__(cls)
        it.init(*args, **kwds)
        return it

    def init(self, *args, **kwds):
        pass


