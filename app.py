from flask import Flask, request, render_template
import os
from flask_cors import CORS, cross_origin

import textToSpeech

app = Flask(__name__)
CORS(app)

@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    data = request.json['data']
    result = textToSpeech.convert(data)
    return {"data" : result.decode("utf-8")}


#port = int(os.getenv("PORT"))
if __name__ == "__main__":
    app.run(host='127.0.0.1')