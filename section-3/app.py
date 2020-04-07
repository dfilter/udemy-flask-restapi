from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [{'name': 'Flask shop', 'items': [{'name': 'flask', 'price': 13.99}]}]


@app.route('/')
def index():
    return 'hello world!'


@app.route('/stores', methods=['POST'])
def create_store():
    request_data = request.get_json()
    store = dict(name=request_data['name'], items=[])
    stores.append(store)
    return jsonify(store)


@app.route('/stores/<string:name>')
def read_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify(message='Store not found.')


@app.route('/stores')
def read_stores():
    return jsonify(stores=stores)


@app.route('/stores/<string:name>/items', methods=['POST'])
def create_store_item(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            item = dict(name=request_data['name'], price=request_data['price'])
            store['items'].append(item)
            return jsonify(item=item)
    return jsonify(message='Store not found.')


@app.route('/stores/<string:name>/items')
def read_store_items(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(items=store['items'])
    return jsonify(message='Store not found.')


app.run()
