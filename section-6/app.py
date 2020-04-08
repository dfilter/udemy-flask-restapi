from datetime import timedelta

from flask import Flask
from flask_jwt import JWT
from flask_restful import Api

from resources.item import Item, Items
from resources.user import UserRegister
from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'secret-key'
app.config['JWT_EXPIRATION_DELTA'] = timedelta(hours=12)

api = Api(app)
# Creates endpoint /auth that returns a jwt token
jwt = JWT(app, authenticate, identity)

api.add_resource(Item, '/item/<string:name>')
api.add_resource(Items, '/items')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
