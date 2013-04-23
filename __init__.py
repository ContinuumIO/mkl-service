"""
MKL module, which exposes a few functions which are declared in
mkl_service.h.
"""

from .service import (get_version_string, mem_stat, get_cpu_clocks,
                      get_cpu_frequency, set_num_threads, get_max_threads)


__version__ = '__VERSION__'
