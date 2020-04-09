import os
from datetime import timedelta

from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restful import Api

from resources.item import Item, Items
from resources.store import Store, Stores
from resources.user import User, UserLogin, UserRegister, TokenRefersh
from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'secret-key'

# "PROPAGATE_EXCEPTIONS" allows flask to show error codes other then
# 500 for flask extentions
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_EXPIRATION_DELTA'] = timedelta(hours=12)

api = Api(app)
# no longer creates /auth endpoint
jwt = JWTManager(app)


@jwt.user_claims_loader
def user_claims_loader(identity):
    # normally of course this wouldn't be hard coded it would be in a
    # config file
    if identity == 1:
        return {'is_admin': True}

    return {'is_admin': False}


api.add_resource(UserRegister, '/register')
api.add_resource(UserLogin, '/login')
api.add_resource(User, '/user/<int:user_id>')
api.add_resource(Stores, '/stores')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(Items, '/items')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(TokenRefersh, '/refresh')

if __name__ == '__main__':
    from db import db

    db.init_app(app)

    @app.before_first_request
    def before_first_request():
        db.create_all()

    app.run(debug=True)
