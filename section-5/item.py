import os
import sqlite3

from flask_jwt import jwt_required
from flask_restful import Resource, reqparse

dir_path = os.path.dirname(os.path.realpath(__file__))
database_location = os.path.join(dir_path, 'data.db')

items = []


class Item(Resource):
    # reqparser will make certain fields required in the body of 
    # the request or in the form data of the request
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help='This field is required.')

    @jwt_required()
    def delete(self, name):
        # use the global items variable defined above (python will
        # think me are making a new item variable otherwise)
        global items
        items = list(filter(lambda item: item['name'] != name, items))
        return {'message': 'Item deleted.'}

    @jwt_required()
    def get(self, name):
        connection = sqlite3.connect(database_location)
        cursor = connection.cursor()

        query = "SELECT * FROM items WHERE name=?"
        result = cursor.execute(query, (name, ))
        row = result.fetchone()
        connection.close()

        if row:
            return {'item': {'name': row[0], 'price': row[1]}}
        
        return {'message': 'Item not found'}, 404

    @jwt_required()
    def post(self, name):
        item = next(filter(lambda item: item['name'] == name, items), None)
        if item is not None:
            return {
                'message':
                "An items with name '{}' already exists.".format(name)
            }, 400
        data = Item.parser.parse_args()
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201

    @jwt_required()
    def put(self, name):
        data = Item.parser.parse_args()
        item = next(filter(lambda item: item['name'] == name, items), None)
        if item is None:
            item = {'name': name, 'price': data['price']}
            items.append(item)
        else:
            item.update(data)
        return item


class Items(Resource):
    @jwt_required()
    def get(self):
        return {'items': items}
