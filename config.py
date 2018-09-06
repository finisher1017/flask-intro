# default config
import os

class BaseConfig(object):
	DEBUG = False
	SECRET_KEY = '\x1b\xb8\x81\xe51\xa1\x82\xba\x96_\xd8^r\xd9\xc1\xba{\xe6\xa0\xa8\x9f\xc7gd'
	SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


class TestConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


class DevelopmentConfig(BaseConfig):
	DEBUG = True


class ProductionConfig(BaseConfig):
	DEBUG = False