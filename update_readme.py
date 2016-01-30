from __future__ import print_function
import os
import re
import doctest
try:
    from cStringIO import StringIO
except:
    from io import StringIO

import mkl


fo = StringIO()


sig_pat = re.compile(r'(\w+\([^()]*\))( -> (.+))?')
def write_doc(name):
    doc = eval('%s.__doc__' % name)
    lines = doc.splitlines()
    m = sig_pat.match(lines[0])
    if m is None:
        raise Exception("signature line invalid: %r" % lines[0])
    s = '``mkl.%s``' %  m.group(1)
    if m.group(3):
        s += ' -> %s' % m.group(3)
    fo.write(s + '\n')
    assert lines[1] == ''
    for line in lines[2:]:
        fo.write('   %s\n' % line)
    fo.write('\n\n')


def write_reference():
    fo.write("Reference\n"
             "---------\n\n"
             "**mkl service functions:**\n\n")
    for method in sorted(dir(mkl)):
        if method.startswith('_') or method == 'service':
            continue
        write_doc('mkl.%s' % method)


def write_all(data):
    ver_pat = re.compile(r'(mkl.+?)(\d+\.\d+)')
    for line in data.splitlines():
        if line == 'Reference':
            break
        line = ver_pat.sub(lambda m: m.group(1) + mkl.__version__, line)
        fo.write(line + '\n')

    write_reference()


def main():
    data = open('README.rst').read()
    write_all(data)
    new_data = fo.getvalue()
    fo.close()

    if new_data == data:
        print("already up-to-date")
    else:
        with open('README.rst', 'w') as f:
            f.write(new_data)

    doctest.testfile('README.rst')


if __name__ == '__main__':
    main()
