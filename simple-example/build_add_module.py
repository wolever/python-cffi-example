import os
from cffi import FFI

cwd = os.path.join(os.path.dirname(__file__), ".")

ffi = FFI()

ffi.set_source("_add_module",
    '#include <add.h>',
    libraries=["add"],
    library_dirs=[cwd],
    include_dirs=[cwd],
)

ffi.cdef("int add(int a, int b);")

if __name__ == "__main__":
    ffi.compile()

