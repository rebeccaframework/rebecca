import unittest
from pyramid import testing

class GirdTests(unittest.TestCase):
    def _getTarget(self):
        from ..helpers import Grid
        return Grid

    def _makeOne(self, *args, **kwargs):
        return self._getTarget()(*args, **kwargs)

    def test_it(self):
        import operator as op
        columns = [
            (u'Name', op.attrgetter('name')),
            (u'Age', op.attrgetter('age')),
        ]
        target = self._makeOne(columns, {"class": "table"})

        items = [testing.DummyModel(name=u"name {0}".format(i), age=20+i)
            for i in range(2)]

        result = target(items)
        self.assertEqual(result, 
            u'<table class="table"><tr><th>Name</th><th>Age</th></tr><tr><td>name 0</td><td>20</td></tr><tr><td>name 1</td><td>21</td></tr></table>')
