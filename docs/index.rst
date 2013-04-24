===========
mkl-service
===========

This package exposes a few functions which are declared in mkl_service.h.

Exmaple:
--------

   >>> import mkl
   >>> mkl.get_max_threads()
   2


Reference
---------

**mkl service functions:**

``mkl.get_cpu_clocks()`` -> int
   Return the CPU clocks as an integer.


``mkl.get_cpu_frequency()`` -> float
   Return CPU frequency in GHz as a float.


``mkl.get_max_threads()`` -> int
   Return the number threads Intel MKL is targeting for parallelism.


``mkl.get_version_string()`` -> str
   Return the library version information as a string.


``mkl.mem_stat(n)`` -> int
   Returns an amount of memory, allocated by the MKL Memory Allocator.


``mkl.set_num_threads(n)``
   Set the number of threads MKL should use.  This is only a hint, and no
   guaranteed is made this number of threads will actually be used.
   This function takes precedence over MKL_NUM_THREADS.


