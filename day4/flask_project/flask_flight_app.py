from flask import Flask, jsonify, request
from dao_oprs import create_table_flights, create_flight, delete_flight, update_flight, search_flight, list_flights, Flight

create_table_flights()

app = Flask(__name__)

@app.route('/flights',methods=['POST'])
def flights_create():
    body = request.get_json()
    new_flight = Flight(body['airline'], body['source'], body['destination'], body['duration'], body['fare'])
    id = create_flight(new_flight)
    flight = search_flight(id)
    flight_dict = {'id':flight.id, 'airline':flight.airline, 'source':flight.source, 'destination':flight.destination, 'duration': flight.duration, 'fare': flight.fare}
    return jsonify(flight_dict)

@app.route('/flights/<id>',methods=['GET'])
def flights_read_by_id(id):
    flight = search_flight(id)
    flight_dict = {'id':flight.id, 'title':flight.airline, 'source':flight.source, 'destination':flight.destination, 'duration': flight.duration, 'fare': flight.fare}
    return jsonify(flight_dict)

@app.route('/flights',methods=['GET'])
def flights_read_all():
    flights = list_flights()
    flights_dict = []
    for flight in flights:
        flights_dict.append({'id':flight.id, 'airline':flight.airline, 'source':flight.source, 'destination':flight.destination, 'duration': flight.duration, 'fare': flight.fare})
    return jsonify(flights_dict)

@app.route('/flights/<id>',methods=['PUT'])
def flights_update(id):
    body = request.get_json()
    old_flight = search_flight(id)
    if not old_flight:
        return jsonify({'message': 'Flight not found'})
    old_flight.airline = body['airline']
    old_flight.source = body['source']
    old_flight.destination = body['destination']
    old_flight.duration = body['duration']
    old_flight.fare = body['fare']
    update_flight(old_flight)
    flight = search_flight(id)
    flight_dict = {'id':flight.id, 'title':flight.airline, 'source':flight.source, 'destination':flight.destination, 'duration': flight.duration, 'fare': flight.fare}
    return jsonify(flight_dict)

@app.route('/flights/<id>',methods=['DELETE'])
def flights_delete(id):
    old_flight = search_flight(id)
    if not old_flight:
        return jsonify({'message': 'Flight not found', 'is_error': 1})
    delete_flight(id)
    return jsonify({'message': 'Flight is deleted', 'is_error': 0})

app.run(debug=True)

'''
@app.route('/flights_search',methods=['POST'])
def flights_search():
    body = request.get_json()
    flights = search(body.get('title',''), body.get('notes_text',''))
    flights_dict = []
    for flight in flights:
        flights_dict.append({'id':flight.id, 'airline':flight.airline, 'source':flight.source, 'destination':flight.destination, 'duration': flight.duration, 'fare': flight.fare})
    return jsonify(flights_dict)
'''