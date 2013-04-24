"""
MKL module, which exposes a few functions which are declared in
mkl_service.h.
"""

from .service import (get_version_string, mem_stat, get_cpu_clocks,
                      get_cpu_frequency, set_num_threads, get_max_threads)


__version__ = '1.0'


def test(verbosity=1):
    """test(verbosity=1) -> TextTestResult

Run self-test, and return unittest.runner.TextTestResult object.
"""
    from .test import run
    return run(verbosity=verbosity)
