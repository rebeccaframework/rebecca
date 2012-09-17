from rebecca.views import ListView
from .models import User
from rebecca.sqla import DBSession
from rebecca.helpers import Grid
from rebecca import helpers
from pyramid.view import view_config

@view_config(route_name='users', renderer='templates/users.pt')
class UserListView(ListView):
    model = User
    session = DBSession
    grid = Grid([
                 (u'', helpers.checkboxmaker('user_name')),
                 (u'#', 'id'),
                 (u'Name', helpers.linkmaker('user_name', 
                           helpers.urlmaker('user', [('user_name', 'user_name')]))),
                ],
                table_attrs={'class': 'table table-striped'})
