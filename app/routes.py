from app import app
from flask import render_template, request,redirect,flash, Response, jsonify

from joblib import load

def predicting_price(rooms, area, house_type, latitude, longitude):
    predictor = load("Regressor.joblib")

    price = predictor.predict([[rooms, area, house_type, latitude, longitude]])
    # price = predictor.predict([[3 ,85.0,1,-5.0888, 39.1023]])
    return price



@app.route('/')
def home():
    return render_template("index.html")



@app.route('/predict', methods=["POST"])
def predict():
    request_data = request.get_json()
    # number of rooms, floor area, house type, latitude, longitude
    number_of_rooms = request_data['number_of_rooms']
    floor_area = request_data['floor_area']
    house_type = request_data['house_type']
    latitude = request_data['latitude']
    longitude = request_data['longitude']
    print(request_data)
    y_value = predicting_price(number_of_rooms, floor_area, house_type, latitude, longitude)
    print(y_value)


    # return jsonify({"price": y_value})
    return jsonify({"price": y_value[0]})

    




    