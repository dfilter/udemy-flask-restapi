from flask import Flask
from flask_jwt import JWT
from flask_restful import Api

from item import Item, Items
from security import authenticate, identity
from user import UserRegister

app = Flask(__name__)
app.secret_key = 'secret-key'

api = Api(app)
# Creates endpoint /auth that returns a jwt token
jwt = JWT(app, authenticate, identity)

api.add_resource(Item, '/item/<string:name>')
api.add_resource(Items, '/items')
api.add_resource(UserRegister, '/register')

app.run(port=5000, debug=True)