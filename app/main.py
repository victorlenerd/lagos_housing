from flask import Flask, request, render_template, jsonify
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    lekki = pd.DataFrame({
        'lng': [6.4698],
        'lat': [3.5852],
        'no_bed': [1],
        'no_toilets': [1],
        'no_bath': [1]
    })
    model = pickle.load(open('./model/model.pkl', 'rb'))
    prediction = model.predict(lekki)
    cost = prediction[0]

    return jsonify(price=cost)

if __name__ == '__main__':
	app.run()