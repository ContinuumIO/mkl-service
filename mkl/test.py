import sys
import unittest

import mkl


class Test(unittest.TestCase):
    _int_long = (int, long) if sys.version_info[0] == 2 else int

    def test_cpu_clocks(self):
        self.assertTrue(isinstance(mkl.get_cpu_clocks(), self._int_long))

    def test_cpu_frequency(self):
        self.assertTrue(isinstance(mkl.get_cpu_frequency(), float))

    def test_set_num_threads(self):
        self.assertRaises(TypeError, mkl.set_num_threads, '2')
        self.assertRaises(ValueError, mkl.set_num_threads, -1)
        self.assertRaises(ValueError, mkl.set_num_threads, 0)

    def test_get_max_threads(self):
        self.assertTrue(isinstance(mkl.get_max_threads(), int))

    def test_mem_stat(self):
        result = mkl.mem_stat()

        self.assertTrue(isinstance(result, tuple))
        self.assertTrue(isinstance(result[0], self._int_long))
        self.assertTrue(isinstance(result[1], self._int_long))


def run(verbosity=1):
    print("sys.prefix: %s" % sys.prefix)
    print("sys.version: %s" % sys.version)
    print("mkl-service version: %r" % mkl.__version__)
    print("MKL version string: %r" % mkl.get_version_string())
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(Test))

    runner = unittest.TextTestRunner(verbosity=verbosity)
    return runner.run(suite)


if __name__ == '__main__':
    run()
