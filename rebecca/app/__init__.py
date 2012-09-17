#
import operator as op
from pyramid.config import Configurator

from ..views import list_view
from .. import helpers


def register_helper(event):
    event.update({'h': helpers})



def main(global_conf, **settings):
    config = Configurator(settings=settings)
    config.add_route('users', '/users')
    config.add_route('user', '/users/{user_name}')
    config.add_subscriber(register_helper, 'pyramid.events.BeforeRender')

    config.scan(".views")

    return config.make_wsgi_app()
