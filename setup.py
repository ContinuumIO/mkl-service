import sys
from os.path import join
from distutils.core import setup
from distutils.extension import Extension


if sys.platform == 'win32':
    mkl_prefix = join(sys.prefix, 'Library')
else:
    mkl_prefix = sys.prefix

setup(
    name='mkl-service',
    author = "Continuum Analytics, Inc.",
    author_email = "support@continuum.io",
    license = "BSD",
    description = "Continuum Analytics MKL service binding",
    packages = ["mkl"],
    ext_modules = [Extension(
            name = "mkl.service",
            sources = ["mkl/service.c"],
            libraries = ["mkl_rt"],
            define_macros = [],
            include_dirs = [join(mkl_prefix, 'include')],
            library_dirs = [join(mkl_prefix, 'lib')],
    )],
)
