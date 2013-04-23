import os
import sys
from os.path import join
from distutils.core import setup
from distutils.extension import Extension


mkl_libs = {
    'linux-64': "mkl_intel_lp64 mkl_intel_thread mkl_core iomp5",
    'linux-32': "mkl_intel mkl_intel_thread mkl_core iomp5",
    'osx-64': "mkl_core mkl_intel_lp64 mkl_intel_thread mkl_mc mkl_mc3",
    'win-64': "mkl_core_dll mkl_intel_lp64_dll mkl_intel_thread_dll",
    'win-32': "mkl_core_dll mkl_intel_c_dll mkl_intel_thread_dll",
}

ext_kwds = dict(
    name = "mkl.service",
    sources = ["service.c"],
    libraries = mkl_libs[os.getenv('SUBDIR')].split(),
    define_macros = [],
    include_dirs = [join(sys.prefix, 'include')],
    library_dirs = [join(sys.prefix,
                         'libs' if sys.platform == 'win32' else 'lib')]
)

setup(
    name='mkl-service',
    author = "Continuum Analytics, Inc.",
    author_email = "support@continuum.io",
    description = "Continuum Analytics MKL service binding",
    packages = ["mkl"],
    ext_modules = [Extension(**ext_kwds)],
)
