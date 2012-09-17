import sqlalchemy as sa
import sqlalchemy.orm as orm

_bind = sa.create_engine('sqlite:///')
_TestingSession = orm.sessionmaker()
_TestingSession.configure(bind=_bind)

_metadata = sa.MetaData()

def _setUp():
    return _TestingSession()

def _tearDown():
    session =  _TestingSession()
    session.rollback()

person_table = sa.Table('person', _metadata,
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('name', sa.Unicode(255), unique=True),
)

class Person(object):
    """ """
    def __init__(self, name=None):
        self.name = name

orm.mapper(Person, person_table)

_metadata.create_all(bind=_bind)
