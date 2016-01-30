"""
This package exposes a few functions which are declared in mkl_service.h.
The main purpose of the package is to allow the user to change the number
of CPU's MKL is using at runtime.
"""

from .service import (get_version_string, mem_stat, get_cpu_clocks,
                      get_cpu_frequency, set_num_threads, get_max_threads)


__version__ = '1.1.2'
