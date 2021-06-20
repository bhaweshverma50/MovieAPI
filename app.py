from flask import Flask, request, jsonify
from flask_cors import CORS
import recommendation
import music

app = Flask(__name__)
CORS(app)


@app.route('/movie', methods=['GET'])
def recommend_movies():
    res = recommendation.results(request.args.get('title'))
    return jsonify(res)


@app.route('/music', methods=['GET'])
def recommend_music():
    res = music.recom(request.args.get('track'))
    return jsonify(res)


@app.route('/', methods=['GET'])
def home():
    return '<h3>Recommender API running!</h3>'


if __name__ == '__main__':
    app.run()
