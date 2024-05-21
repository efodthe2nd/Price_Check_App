import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
  SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard_to_get_string'

  def init_app(self):
    pass


class Development(Config):
  DEBUG = True

class Testing(Config):
  TESTING = True

class Production(Config):
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'data.sqlite')

config = {
  'developmentConfig' : Development,
  'testingConfig' : Testing,
  'productionConfig' : Production,
  'defaultConfig' : Development
}