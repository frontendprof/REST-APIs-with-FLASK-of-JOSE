# B_R_R
# M_S_A_W

from flask import Flask, jsonify, request

app=Flask(__name__)


stores=[
    { 'name': 'My Pretty Store',
        'items':[
        {
        'name': 'item1',
        'price':15
        }
        ]

}
]
@app.route('/store', methods=['POST'])
def create_store():
    request_data=request.get_json()
    new_store={
    'name':request_data['name'],
    'items':[]
    }
    stores.append(new_store)
    return jsonify(new_store)


@app.route('/store/<string:name>', methods=['GET'])
def get_store(name):
    for store in stores:
        if store['name']==name:
            return jsonify(store)
    return  jsonify({'message':'store not found'})


@app.route('/store')
def get_stores():
    return jsonify({'stores':stores})


@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data=request.get_json()
    for store in stores:
        if store['name']==name:
            new_item={
            'name':request_data['name'],
            'price':request_data['price']
            }
            store['itmes'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message':'store not found'})


@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for store in stores:
        if store['name']==name:
            return jsonify({'items': store['items']})
    return jsonify({'message': 'store not found '})





app.run(port=5000)
