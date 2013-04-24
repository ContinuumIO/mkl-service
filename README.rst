===========
mkl-service
===========

This package exposes a few functions which are declared in mkl_service.h.


Reference
---------

**mkl service functions:**

``get_cpu_clocks()`` -> int
   Return the CPU clocks as an integer.


``get_cpu_frequency()`` -> float
   Return CPU frequency in GHz as a float.


``get_max_threads()`` -> int
   Return the number threads Intel MKL is targeting for parallelism.


``get_version_string()`` -> str
   Return the library version information as a string.


``mem_stat(n)`` -> int
   Returns an amount of memory, allocated by the MKL Memory Allocator.


``set_num_threads(n)``
   Set the number of threads MKL should use.  This is only a hint, and no
   guaranteed is made this number of threads will actually be used.
   This function takes precedence over MKL_NUM_THREADS.


``test(verbosity=1)`` -> TextTestResult
   Run self-test, and return unittest.runner.TextTestResult object.


