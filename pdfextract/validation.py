# -*- coding: utf-8 -*-

import os
import subprocess

def is_program_installed(program_name):
    '''Determines if a given program is installed by checking if calling
    subprocess with its program executable as parameter yields a file not
    found error. If subprocess terminates with file not found or some
    different error, we assume that the given program is not installed
    on the system.

    Arguments:
        program_name    --      Name of the executable

    Returns:
        True if the program is installed, False otherwise
    '''
    is_installed = True
    try:
        FNULL = open(os.devnull, 'w')
        subprocess.call([program_name], stdout=FNULL, stderr=subprocess.STDOUT)
        FNULL.close()
    except OSError as e:
        if e.errno == os.errno.ENOENT:
            # not found
            is_installed = False
        else:
            # something else went wrong
            is_installed = False
    return is_installed