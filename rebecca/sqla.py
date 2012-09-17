"""
Utilities for SQLAlchemy
"""

import sqlalchemy as sa
import sqlalchemy.orm as orm
import operator
from zope.interface import implementer
from zope.sqlalchemy import ZopeTransactionExtension
from .interfaces import IList


@implementer(IList)
class QueryAdapter(object):
    
    def __init__(self, session, model):
        self.session = session
        self.model = model
        self.query = session.query(model)

    def __len__(self):
        return self.query.count()

    def __getitem__(self, index):
        return operator.getitem(self.query, index)

    def __iter__(self):
        return iter(self.query)

DBSession = None

def includeme(config):
    global DBSession
    engine = sa.engine_from_config(config.registry.settings)
    if DBSession is None:
        DBSession = orm.scoped_session(
            orm.sessionmaker(extension=ZopeTransactionExtension()))

    DBSession.remove()
    DBSession.configure(bind=engine)
