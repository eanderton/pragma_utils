'''
Small functions that cover small corner cases.
'''

import os
import stat


def to_bool(value):
    ''' Converts any value to a boolean. '''
    return str(value).lower() == "true"


def is_piped_stdin():
    ''' Returns true if stdin is on a pipe '''
    mode = os.fstat(sys.stdin.fileno()).st_mode
    return stat.S_ISFIFO(mode) or stat.S_ISREG(mode)


def is_piped():
    ''' Returns true if the program has either stdin or stdout on a pipe.'''
    return os.fstat(0) != os.fstat(1)

