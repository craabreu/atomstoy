from os.path import dirname
from os.path import join

from cffi import FFI

ffi = FFI()
ffi.cdef('''
    char* longest(int argv, char *argv[]);
''')

ffi.set_source(
    'atomstoys._atomstoys',
    open(join(dirname(__file__), '_atomstoys.c')).read()
)

if __name__ == '__main__':
    ffi.compile()
