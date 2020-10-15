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
