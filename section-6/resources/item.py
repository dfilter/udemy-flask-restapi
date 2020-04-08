import os
import sqlite3

from flask_jwt import jwt_required
from flask_restful import Resource, reqparse

from models.item import ItemModel

dir_path = os.path.dirname(os.path.realpath(__file__))
database_location = os.path.join(dir_path, 'data.db')


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
        connection = sqlite3.connect(database_location)
        cursor = connection.cursor()
        query = "DELETE FROM items WHERE name=?"
        cursor.execute(query, (name, ))
        connection.commit()
        connection.close()
        return {'message': 'Item deleted.'}

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()

        return {'message': 'Item not found'}, 404

    @jwt_required()
    def post(self, name):
        if ItemModel.find_by_name(name):
            return {
                'message':
                "An items with name '{}' already exists.".format(name)
            }, 400

        data = Item.parser.parse_args()
        item = ItemModel(name, data['price'])
        try:
            item.insert()
        except:
            return {'message': 'An error occurred inserting the item.'}, 500

        return item, 201

    @jwt_required()
    def put(self, name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)
        updated_item = ItemModel(name, data['price'])
        if item:
            try:
                updated_item.update()
            except:
                return {'message': 'An error occurred updating the item.'}, 500

        else:
            try:
                updated_item.insert()
            except:
                return {
                    'message': 'An error occurred inserting the item.'
                }, 500

        return updated_item.json()


class Items(Resource):
    @jwt_required()
    def get(self):
        connection = sqlite3.connect(database_location)
        cursor = connection.cursor()

        query = "SELECT * FROM items"
        result = cursor.execute(query)
        items = []
        for row in result:
            items.append({'name': row[0], 'price': [1]})
        row = result.fetchall()
        connection.close()

        return {'items': items}
