from flask import Flask, request, jsonify
from db import create_reservation, get_reservation_by_id, update_reservation, delete_reservation
from datetime import datetime

app = Flask(__name__)

@app.route('/reservations', methods=['POST'])
def create_new_reservation():
    data = request.json
    diner_username = data.get('diner_username')
    restaurant_name = data.get('restaurant_name')
    reservation_time_str = data.get('reservation_time')
    number_of_people = data.get('number_of_people')
    status = data.get('status')

    reservation_time = datetime.strptime(reservation_time_str, '%Y-%m-%d %H:%M:%S')

    reservation_id = create_reservation(diner_username, restaurant_name, reservation_time, number_of_people, status)
    if reservation_id:
        return jsonify({'reservation_id': reservation_id}), 201
    else:
        return jsonify({'error': 'Reservation could not be created'}), 500

@app.route('/reservations/<int:reservation_id>', methods=['GET'])
def get_reservation(reservation_id):
    reservation = get_reservation_by_id(reservation_id)
    if reservation:
        return jsonify(reservation), 200
    else:
        return jsonify({'error': 'Reservation not found'}), 404

@app.route('/reservations/<int:reservation_id>', methods=['PUT'])
def update_existing_reservation(reservation_id):
    data = request.json
    diner_username = data.get('diner_username')
    restaurant_name = data.get('restaurant_name')
    reservation_time_str = data.get('reservation_time')
    number_of_people = data.get('number_of_people')
    status = data.get('status')

    reservation_time = datetime.strptime(reservation_time_str, '%Y-%m-%d %H:%M:%S')

    success = update_reservation(reservation_id, diner_username, restaurant_name, reservation_time, number_of_people, status)
    if success:
        return jsonify({'success': True}), 200
    else:
        return jsonify({'error': 'Reservation could not be updated'}), 500

@app.route('/reservations/<int:reservation_id>', methods=['DELETE'])
def delete_existing_reservation(reservation_id):
    success = delete_reservation(reservation_id)
    if success:
        return jsonify({'success': True}), 200
    else:
        return jsonify({'error': 'Reservation could not be deleted'}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
