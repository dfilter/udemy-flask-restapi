from flask_jwt_extended import (get_jwt_claims, get_jwt_identity, jwt_optional,
                                jwt_required)
from flask_restful import Resource, reqparse

from models.item import ItemModel


class Item(Resource):
    # reqparser will make certain fields required in the body of
    # the request or in the form data of the request
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help='This field is required.')
    parser.add_argument('store_id',
                        type=int,
                        required=True,
                        help='This field is required.')

    @jwt_required
    def delete(self, name):
        claims = get_jwt_claims()
        if not claims['is_admin']:
            return {'message': 'Admin privilege required.'}, 401
        
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()

        return {'message': 'Item Deleted.'}

    @jwt_required
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()

        return {'message': 'Item not found'}, 404

    @jwt_required
    def post(self, name):
        if ItemModel.find_by_name(name):
            return {
                'message':
                "An items with name '{}' already exists.".format(name)
            }, 400

        data = Item.parser.parse_args()
        item = ItemModel(name, **data)
        try:
            item.save_to_db()
        except:
            return {'message': 'An error occurred inserting the item.'}, 500

        return item.json(), 201

    @jwt_required
    def put(self, name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)
        if item:
            item.price = data['price']
        else:
            item = ItemModel(name, **data)

        item.save_to_db()
        return item.json()


class Items(Resource):
    @jwt_optional
    def get(self):
        # Get the user's id from jwt token see UserLogin resource (identity)
        user_id = get_jwt_identity()
        items = [item.json() for item in ItemModel.find_all()]
        if user_id:
            return {'items': items}

        return {
            'item': [item['name'] for item in items],
            'message': 'More data available if you login.'
        }
