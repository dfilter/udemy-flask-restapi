from flask import Flask, request
from flask_jwt import JWT, jwt_required
from flask_restful import Resource, Api

from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'secret-key'

api = Api(app)
# Creates endpoint /auth that returns a jwt token
jwt = JWT(app, authenticate, identity)

items = []


class Item(Resource):
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
        data = request.get_json()
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201

    @jwt_required()
    def put(self, name):
        data = request.get_json()
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
