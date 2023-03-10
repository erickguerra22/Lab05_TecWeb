#!/usr/bin/python

import db
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask('chat')
CORS(app, resources = {r"/*":{"origins": "*"}})

@app.route('/messages', methods = ['GET'])
def GET_messages():
    return jsonify(db.get_messages())

@app.route('/messages', methods = ['POST'])
def POST_messages():
    message = request.get_json()
    return jsonify(db.create_message(message))

if __name__ == "__main__":
    app.run(debug=True)