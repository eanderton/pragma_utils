'''
Decorators to cover various corner-casess in Python.
'''

from inspect import signature

def mapped_args(fn):
    ''' Function wrapper that only passes kwargs that map to the wrapped function. '''

    def impl(**kwargs):
        fn_kwargs={}
        for k in signature(fn).parameters:
            fn_kwargs[k] = kwargs[k]
        fn(**fn_kwargs)

    return impl

def selfish(*attr_names):
    ''' Maps attributes of self on a member function to kwargs of the same name. '''

    def deco(fn):
        def impl(self, *args, **kwargs):
            fn_kwargs = dict(kwargs)
            for name in attr_names:
                if name in signature(fn).parameters:
                    fn_kwargs[name] = getattr(self, name)
            return fn(self, *args, **fn_kwargs)
        return impl
    return deco
