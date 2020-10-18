class FeatureFlag(object):
    '''
    Basic feature flag implementation. Used to turn on/off library features.

    As a bool wrapper, this may be safely used as a default value in library
    methods and functions for run-time evaluation of a default argument.

    >>> from pragma_utils import FeatureFlag
    >>> optional_feature = FeatureFlag(false)
    >>>
    >>> # enable the flag
    >>> optional_feature.enable()
    >>>
    >>> # test the flag to enable featured behavior
    >>> if optional_feature:
    >>>     print('Feature enabled')
    '''

    def __init__(self, value=False):
        self.value = bool(value)

    def __bool__(self):
        return self.value

    def __nonzero__(self):
        return self.__bool__()

    def enable(self):
        self.value = True

    def disable(self):
        self.value = False
