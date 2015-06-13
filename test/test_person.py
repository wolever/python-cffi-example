from cffi_example.person import Person

class TestPerson(object):
    def setup(self):
        self.p = Person(u"Alex", u"Smith", 72)

    def test_get_age(self):
        assert self.p.get_age() == 72

    def test_get_full_name(self):
        assert self.p.get_full_name() == u"Alex Smith"

    def test_long_name(self):
        p = Person(u"x" * 100, u"y" * 100, 72)
        assert p.get_full_name() == u"x" * 100
