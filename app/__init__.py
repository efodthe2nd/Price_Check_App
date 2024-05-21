#we build an application factory here
from flask import Flask
from config import config
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()

def create_app():
  app = Flask(__name__)
  configname = 'defaultConfig'
  app.config.from_object(config[configname])
  config[configname].init_app(app)

  bootstrap.init_app(app)

  from .main import main as main_blueprint
  app.register_blueprint(main_blueprint)


  return app
