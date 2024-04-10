from flask import Flask, request, jsonify
import db

app = Flask(__name__)

@app.route('/restaurants', methods=['POST'])
def create_restaurant():
    data = request.get_json()
    owner_username = data.get('owner_username')
    restaurant_name = data.get('restaurant_name', '')
    address = data.get('address', '')
    phone = data.get('phone', '')
    email = data.get('email', '')
    
    restaurant_id = db.create_restaurant(owner_username, restaurant_name, address, phone, email)
    if restaurant_id:
        return jsonify({'restaurant_id': restaurant_id}), 201
    else:
        return jsonify({'error': 'Failed to create restaurant'}), 500

@app.route('/restaurants/<int:restaurant_id>', methods=['GET'])
def get_restaurant(restaurant_id):
    restaurant = db.get_restaurant_by_id(restaurant_id)
    if restaurant:
        return jsonify(restaurant), 200
    else:
        return jsonify({'error': 'Restaurant not found'}), 404

@app.route('/restaurants/<int:restaurant_id>', methods=['PUT'])
def update_restaurant(restaurant_id):
    data = request.get_json()
    owner_username = data.get('owner_username')
    restaurant_name = data.get('restaurant_name', '')
    address = data.get('address', '')
    phone = data.get('phone', '')
    email = data.get('email', '')
    
    success = db.update_restaurant(restaurant_id, owner_username, restaurant_name, address, phone, email)
    if success:
        return jsonify({'success': True}), 200
    else:
        return jsonify({'error': 'Failed to update restaurant'}), 500

@app.route('/restaurants/<int:restaurant_id>', methods=['DELETE'])
def delete_restaurant(restaurant_id):
    success = db.delete_restaurant(restaurant_id)
    if success:
        return jsonify({'success': True}), 200
    else:
        return jsonify({'error': 'Failed to delete restaurant'}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
