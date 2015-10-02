/*
  Copyright (c) 2013, Ilan Schnell, Continuum Analytics, Inc.
  Python bindings to some MKL service functions, see: mkl_service.h

  TODO -- other functions to look at in mkl_service.h:
    - mkl_enable_instructions
    - mkl_peak_mem_usage
*/

#include "Python.h"
#include "mkl_service.h"

#if PY_MAJOR_VERSION >= 3
#define IS_PY3K
#define PyInt_FromLong  PyLong_FromLong
#endif


static PyObject *
get_version_string(void)
{
    char buffer[256];

    mkl_get_version_string(buffer, sizeof(buffer));
    return PyUnicode_FromString(buffer);
}

PyDoc_STRVAR(doc_get_version_string, "get_version_string() -> str\n\n\
Return the MKL library version information as a string.");


static PyObject *
mem_stat(PyObject *self, PyObject *args)
{
    PyObject *result_tuple;
    MKL_INT64 bytes;
    int blocks;

    bytes = mkl_mem_stat(&blocks);

    result_tuple = PyTuple_New(2);
    PyTuple_SET_ITEM(result_tuple, 0, PyLong_FromLongLong((PY_LONG_LONG) bytes));
    PyTuple_SET_ITEM(result_tuple, 1, PyLong_FromLong(blocks));

    return result_tuple;
}

PyDoc_STRVAR(doc_mem_stat, "mem_stat() -> (int, int)\n\n\
Returns a tuple (bytes, count) containing memory usage statistics of the\n\
MKL allocator\n\
- number of bytes allocated (bytes).\n\
- number of allocated blocks (count).");


static PyObject *
get_cpu_clocks(void)
{
    unsigned MKL_INT64 x;

    mkl_get_cpu_clocks(&x);
    return PyLong_FromUnsignedLongLong((unsigned PY_LONG_LONG) x);
}

PyDoc_STRVAR(doc_get_cpu_clocks, "get_cpu_clocks() -> int\n\n\
Return the CPU clocks as an integer.");


static PyObject *
get_cpu_frequency(void)
{
    return PyFloat_FromDouble(mkl_get_cpu_frequency());
}

PyDoc_STRVAR(doc_get_cpu_frequency, "get_cpu_frequency() -> float\n\n\
Return CPU frequency in GHz as a float.");


static PyObject *
set_num_threads(PyObject *self, PyObject *args)
{
    int n;

    if (!PyArg_ParseTuple(args, "i", &n)) {
        return NULL;
    }
    if (n < 1) {
        PyErr_SetString(PyExc_ValueError, "positive integer expected");
        return NULL;
    }
    mkl_set_num_threads(n);
    Py_RETURN_NONE;
}

PyDoc_STRVAR(doc_set_num_threads , "set_num_threads(n)\n\n\
Set the number of threads MKL should use.  This is only a hint, and no\n\
guaranteed is made this number of threads will actually be used.\n\
This function takes precedence over the environment variable\n\
MKL_NUM_THREADS.");


static PyObject *
get_max_threads(void)
{
    return PyInt_FromLong((long) mkl_get_max_threads());
}

PyDoc_STRVAR(doc_get_max_threads, "get_max_threads() -> int\n\n\
Return the number of threads Intel MKL is targeting for parallelism.");


static PyMethodDef module_functions[] = {
#define F(name, func)  {#name, (PyCFunction) name, func, doc_ ##name}
    F(get_version_string, METH_NOARGS),
    F(mem_stat,           METH_NOARGS),
    F(get_cpu_clocks,     METH_NOARGS),
    F(get_cpu_frequency,  METH_NOARGS),
    F(set_num_threads,    METH_VARARGS),
    F(get_max_threads,    METH_NOARGS),
#undef F
    {NULL,                NULL}  /* sentinel */
};

PyDoc_STRVAR(m_doc, "\
Extension module providing service functions for the MKL library");

/* the following line is a marker to insert licensing code */
/*MARK1*/

/* initialization routine for the shared library */
#ifdef IS_PY3K
static PyModuleDef moduledef = {
    PyModuleDef_HEAD_INIT, "service", m_doc, -1, module_functions,
};
PyMODINIT_FUNC PyInit_service(void)
#else
PyMODINIT_FUNC initservice(void)
#endif
{
    PyObject *m;

    /* the following line is a marker to insert licensing code */
    /*MARK2*/

#ifdef IS_PY3K
    m = PyModule_Create(&moduledef);
    if (m == NULL)
        return NULL;
#else
    m = Py_InitModule3("service", module_functions, m_doc);
    if (m == NULL)
        return;
#endif

#ifdef IS_PY3K
    return m;
#endif
}
