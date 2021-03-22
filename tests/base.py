from tornado.testing import AsyncHTTPTestCase
from tornado_sqlalchemy import SQLAlchemy
from tornado.web import Application
from urls import routes
from alembic.command import upgrade as alembic_upgrade
from alembic.config import Config as AlembicConfig

import sys
import os


myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')


class BaseDBTestCase(AsyncHTTPTestCase):
    def setUp(self):
        super(BaseDBTestCase, self).setUp()
        alembic_config = AlembicConfig('alembic.ini')
        alembic_config.set_main_option('sqlalchemy.url', 'sqlite:///testdb.sqlite')
        alembic_upgrade(alembic_config, 'head')

    def tearDown(self):
        os.remove('testdb.sqlite')

    def get_app(self):
        self.engine = SQLAlchemy('sqlite:///testdb.sqlite')
        self.session = self.engine.sessionmaker()
        return Application(routes, db=self.engine, debug=True)
