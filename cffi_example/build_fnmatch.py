import os

from cffi import FFI

ffi = FFI()

ffi.set_source("cffi_example._fnmatch",
    # Since we are calling fnmatch directly no custom source is necessary. We
    # need to #include <fnmatch.h>, though, because behind the scenes cffi
    # generates a .c file which contains a Python-friendly wrapper around
    # ``fnmatch``:
    #    static PyObject *
    #    _cffi_f_fnmatch(PyObject *self, PyObject *args) {
    #        ... setup ...
    #        result = fnmatch(...);
    #        return PyInt_FromLong(result);
    #    }
    # (the complete function is defined in _fnmatch.c which will exist in this
    # directory after building this project).
    # See the "How CFFI Works" heading in the README for a more complete
    # explanation of what's going on under the hood.
    "#include <fnmatch.h>",
    # Tell the compiler to link against libc (ie, ``$CC -lc ...``):
    libraries=["c"],
)

with open(os.path.join(os.path.dirname(__file__), "fnmatch.h")) as f:
    # As part of the build process (see "How CFFI Works" in the README), CFFI
    # uses the pycparser package to parse the definitions in ``ffi.cdef`` and
    # generate Python-friendly wrappers.
    # For example, the definition of fnmatch::
    #     int fnmatch(char *pattern, char *name, int flags);
    # Is used to generate a C function which can be called from Python (see
    # _cffi_f_fnmatch in the example above, or the complete _cffi_f_fnmatch in
    # _fnmatch.c which will exist in this directory after building this
    # project).
    ffi.cdef(f.read())

if __name__ == "__main__":
    ffi.compile()
