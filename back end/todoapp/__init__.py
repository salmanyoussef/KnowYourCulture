from flask import Flask

from .main.routes import main
from .extensions import mongo

def create_app():
  app = Flask(__name__)

  app.config['MONGO_URI'] = 'mongodb+srv://todo:20w7hNr8fTNuHXpL@cluster0.rmzbnbz.mongodb.net/mydb?retryWrites=true&w=majority'

  mongo.init_app(app)

  app.register_blueprint(main)

  return app