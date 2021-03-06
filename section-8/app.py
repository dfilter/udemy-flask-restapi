import os
from datetime import timedelta

from flask import Flask
from flask_jwt import JWT
from flask_restful import Api

from resources.item import Item, Items
from resources.store import Store, Stores
from resources.user import UserRegister
from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'secret-key'
# Use Heroku's DATABASE_URL if it is not found use sqlite db
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_EXPIRATION_DELTA'] = timedelta(hours=12)

api = Api(app)
# Creates endpoint /auth that returns a jwt token
jwt = JWT(app, authenticate, identity)

api.add_resource(UserRegister, '/register')
api.add_resource(Stores, '/stores')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(Items, '/items')
api.add_resource(Item, '/item/<string:name>')
