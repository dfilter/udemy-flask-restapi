import os
from datetime import timedelta

from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from flask_restful import Api

from resources.item import Item, Items
from resources.store import Store, Stores
from resources.user import TokenRefersh, User, UserLogin, UserRegister
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
def user_claims_callback(identity):
    """ This method checks incoming tokens and provides their identity 
    (id) to this callback function. We check to see if their id is 1 
    and if it is we set their jwt claims "is_admin" to True else False 
    """
    # normally of course this wouldn't be hard coded it would be in a
    # config file
    if identity == 1:
        return {'is_admin': True}

    return {'is_admin': False}


@jwt.expired_token_loader
def expired_token_callback():
    """ This method determines what message to send back to the user 
    once they try to use an expired token. """
    return jsonify({
        'descrption': 'The token has expired.',
        'error': 'token_expired'
    }), 401


@jwt.invalid_token_loader
def invalid_token_callback(error):
    """ This method is called if the provided token is invalid  """
    return jsonify({
        'descrption': 'The provided token is invalid.',
        'error': 'token_invalid'
    }), 401


@jwt.unauthorized_loader
def unauthorized_token_callback(error):
    """ No token was provided  """
    return jsonify({
        'descrption': 'Please provide a valid token.',
        'error': 'token_unauthorized'
    }), 401


@jwt.needs_fresh_token_loader
def needs_fresh_token_callback(error):
    """ Provided token must be fresh  """
    return jsonify({
        'descrption': 'The provided token is not fresh please login.',
        'error': 'token_not_fresh'
    }), 401


@jwt.revoked_token_loader
def revoke_token_callback(error):
    """ Provided token has been revoked.  """
    return jsonify({
        'descrption': 'The provided token has been revoked.',
        'error': 'token_revoked'
    }), 401


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
