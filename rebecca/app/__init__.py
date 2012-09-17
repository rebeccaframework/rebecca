#
import operator as op
from pyramid.config import Configurator

from ..views import list_view
from .. import helpers
from webhelpers.html.tags import link_to


def register_helper(event):
    event.update({'h': helpers})


def linkmaker(label_attr, urlmaker):
    def maker(value):
        label = getattr(value, label_attr)
        url = urlmaker(value)
        return link_to(label=label, url=url)

    return maker

def main(global_conf, **settings):
    config = Configurator(settings=settings)
    config.add_route('users', '/users')
    config.add_view(list_view('rebecca.sqla.DBSession', '.models.User',
                        [(u'Name', op.attrgetter('user_name')),
                         (u'Link', linkmaker('user_name', lambda x: '/')),
                        ]), 
        route_name='users',
        renderer="templates/users.pt")
    config.add_subscriber(register_helper, 'pyramid.events.BeforeRender')

    return config.make_wsgi_app()
