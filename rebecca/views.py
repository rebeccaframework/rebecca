from pyramid.path import DottedNameResolver, caller_package
from . import helpers as h
from . import sqla

class ListView(object):
    """ a generic view for SQLAlchemy """


    def __init__(self, request):
        self.request = request

    def __call__(self):
        items = sqla.QueryAdapter(self.session, self.model)
        return dict(items=list(items),
                grid=self.grid(items),
                count=len(items))


def list_view(session, model, columns):
    resolver = DottedNameResolver(caller_package())
    session = resolver.maybe_resolve(session)
    model = resolver.maybe_resolve(model)
    grid = h.Grid(columns)
    View = type(model.__name__ + '_ListView',
        (ListView,), {})
    View.session = session
    View.model = model
    View.grid = grid
    return View
