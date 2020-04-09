import os
import sqlite3

from flask_jwt import jwt_required
from flask_restful import Resource, reqparse

from models.user import UserModel

dir_path = os.path.dirname(os.path.realpath(__file__))
database_location = os.path.join(dir_path, 'data.db')


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help='This field is required.')
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help='This field is required.')
    
    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {'message': 'A user with that username already exists.'}, 400

        user = UserModel(**data)
        user.save_to_db()

        return {'message': 'User created successfully.'}, 201


class User(Resource):
    @jwt_required
    def get(self, user_id):
        user = UserModel.find_by_id(user_id)
        if user:
            return user.json()
        
        return {'message': 'User not found.'}, 404 

    @jwt_required
    def delete(self, user_id):
        user = UserModel.find_by_id(user_id)
        if user:
            user.delete_from_db()
            return {'message': 'User deleted'}

        return {'message': 'User not found.'}, 404
