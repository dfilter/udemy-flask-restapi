from flask import Flask, request
from flask_jwt import JWT, jwt_required
from flask_restful import Resource, Api, reqparse

from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'secret-key'

api = Api(app)
# Creates endpoint /auth that returns a jwt token
jwt = JWT(app, authenticate, identity)

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
        # "next()" gives the first time of a list from the filter function
        item = next(filter(lambda item: item['name'] == name, items), None)
        return {'item': item}, 200 if item else 404

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


api.add_resource(Item, '/item/<string:name>')
api.add_resource(Items, '/items')

app.run(port=5000, debug=True)
