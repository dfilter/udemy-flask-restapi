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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_EXPIRATION_DELTA'] = timedelta(hours=12)

api = Api(app)
# Creates endpoint /auth that returns a jwt token
jwt = JWT(app, authenticate, identity)


@app.before_first_request
def before_first_request():
    db.create_all()


api.add_resource(UserRegister, '/register')
api.add_resource(Stores, '/stores')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(Items, '/items')
api.add_resource(Item, '/item/<string:name>')


if __name__ == '__main__':
    from db import db

    db.init_app(app)
    app.run(port=5000, debug=True)
