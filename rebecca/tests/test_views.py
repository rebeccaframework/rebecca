import unittest
from pyramid import testing
from . import testing_views

class ListViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def _getTarget(self):
        from ..views import ListView
        return ListView

    def _makeOne(self, *args, **kwargs):
        return self._getTarget()(*args, **kwargs)

    def test_it(self):
        items = [
            testing.DummyModel(),
        ]


        request = testing.DummyRequest()
        target = self._makeOne(request)
        target.session = testing_views.DummySession(items)
        target.model = testing.DummyModel
        result = target()


        self.assertEqual(result['count'], 1)
