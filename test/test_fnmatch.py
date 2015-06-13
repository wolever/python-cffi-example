import pytest

from cffi_example import fnmatch

@pytest.mark.parametrize("pattern,name,flags,expected", [
    ("foo", "bar", 0, False),
    ("f*", "foo", 0, True),
    ("f*bar", "f/bar", 0, True),
    ("f*bar", "f/bar", fnmatch.FNM_PATHNAME, False),
])
def test_fnmatch(pattern, name, flags, expected):
    assert fnmatch.fnmatch(pattern, name, flags) == expected
