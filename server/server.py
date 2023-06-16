from flask import Flask, request, jsonify
import util

app = Flask(__name__)


@app.route('/get_state_names')
def get_state_names():
    response = jsonify({
        'state': util.get_state_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/get_season_name')
def get_season_name():
    response = jsonify({
        'season': util.get_season_name()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/get_soil_type')
def get_soil_type():
    response = jsonify({
        'state': util.get_soil_type()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/predict_crop', methods=['GET', 'POST'])
def predict_crop():
    state = request.form.get('state')
    if state is None:
        print("lkkjjhhv")
    season = request.form.get('season')
    soil = request.form.get('soil')
    rainfall = int(request.form.get('rainfall'))

    response = jsonify({
       'predicted_crop': util.predict_crop(state, season, soil, rainfall)
    })

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/predict_crops', methods=['GET', 'POST'])
def predict_crops():
    state = 'Rajasthan'
    season = 'Kharif'
    soil = 'Redclay'
    rainfall = 2800

    response = jsonify({
        'predicted_crop': util.predict_crop(state, season, soil, rainfall)
    })

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == "__main__":
    print("starting flask server")
    app.run()
