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

    @classmethod
    def find_by_name(cls, name):
        connection = sqlite3.connect(database_location)
        cursor = connection.cursor()

        query = "SELECT * FROM items WHERE name=?"
        result = cursor.execute(query, (name, ))
        row = result.fetchone()
        connection.close()

        if row:
            return {'item': {'name': row[0], 'price': row[1]}}

    @classmethod
    def insert(cls, item):
        connection = sqlite3.connect(database_location)
        cursor = connection.cursor()
        query = "INSERT INTO items VALUES (?, ?)"
        cursor.execute(query, (item['name'], item['price']))
        connection.commit()
        connection.close()

    @classmethod
    def update(cls, item):
        connection = sqlite3.connect(database_location)
        cursor = connection.cursor()
        query = "UPDATE items SET price=? WHERE name=?"
        cursor.execute(query, (item['price'], item['name']))
        connection.commit()
        connection.close()

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
        item = self.find_by_name(name)
        if item:
            return item
        
        return {'message': 'Item not found'}, 404

    @jwt_required()
    def post(self, name):
        if self.find_by_name(name):
            return {
                'message':
                "An items with name '{}' already exists.".format(name)
            }, 400
        
        data = Item.parser.parse_args()
        item = {'name': name, 'price': data['price']}
        try:
            self.insert(item)
        except:
            return {'message': 'An error occurred inserting the item.'}, 500

        return item, 201

    @jwt_required()
    def put(self, name):
        data = Item.parser.parse_args()
        item = self.find_by_name(name)
        updated_item = {'name': name, 'price': data['price']}
        if item:
            try:
                self.update(updated_item)
            except:
                return {'message': 'An error occurred updating the item.'}, 500
    
        else:
            try:
                self.insert(updated_item)
            except:
                return {'message': 'An error occurred inserting the item.'}, 500
            
        return updated_item


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
