import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'cBW?F4j6V<K9ZXyG;bw№H;vVn.VJvWCfzUZ)_{:2a2wmkZmz<)Rwl;№h2&o!'
    BOT_TOKEN = '639381913:AAF2kHmbSvIGGDOJNj1-1alwuJRhEsijeMU'
    SQLALCHEMY_DATABASE_URI = "postgres://fkhpuecxdunwyl:a9663a3bf83d85744a55472b82d21d75d63269e1dc0280562c19f97eca4a70ce@ec2-184-73-216-48.compute-1.amazonaws.com:5432/d6nk003ngu86ju"


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
