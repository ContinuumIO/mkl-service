import sys
from os.path import join
from distutils.core import setup
from distutils.extension import Extension


ext_kwds = dict(
    name = "mkl.service",
    sources = ["mkl/service.c"],
    libraries = ["mkl_rt"],
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
