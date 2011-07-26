"""
"""

from __future__ import absolute_import
import redis
from flask import g

class Redis(object):

    def __init__(self, app=None):

        if app is not None:
            self.init_app(app)
        else:
            self.app = None

    def init_app(self, app):
        """
        Used to initialize redis with app object
        """
        app.config.setdefault('REDIS_HOST', 'localhost')
        app.config.setdefault('REDIS_PORT', 6379)
        app.config.setdefault('REDIS_DB', 0)
        app.config.setdefault('REDIS_PASSWORD', None)

        app.before_request(self.before_request)

        self.app = app

    def connect(self):
        return redis.Redis(host=self.app.config['REDIS_HOST'],
                           port=self.app.config['REDIS_PORT'],
                           db=self.app.config['REDIS_DB'],
                           password=self.app.config['REDIS_PASSWORD'])

    def before_request(self):
        g.redis = self.connect()
