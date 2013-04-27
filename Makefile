LIB_DIR=`$(PYTHON)-config --prefix`/lib


mkl/service.so: mkl/service.c
	$(PYTHON) setup.py build_ext --inplace


test: mkl/service.so
	DYLD_LIBRARY_PATH=$(LIB_DIR) LD_LIBRARY_PATH=$(LIB_DIR) \
		$(PYTHON) -c "import mkl.test; mkl.test.run()"


doc: mkl/service.so
	DYLD_LIBRARY_PATH=$(LIB_DIR) LD_LIBRARY_PATH=$(LIB_DIR) \
		$(PYTHON) update_readme.py
	cp README.rst docs/index.rst


clean:
	rm -rf build dist
	rm -f mkl/*.o mkl/*.so
	rm -f mkl/*.pyc
	rm -rf mkl/__pycache__ *.egg-info
	rm -f README.html
