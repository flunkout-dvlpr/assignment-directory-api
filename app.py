import json

from flask import Flask, jsonify, request

app = Flask(__name__)

with open("starter-data.json", "r") as fp:
    employees = json.load(fp)

@app.route("/")
def index():
    return jsonify(employees)

if __name__ == "__main__":
    app.run(debug=True)