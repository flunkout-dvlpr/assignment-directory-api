import json

from flask import Flask, jsonify, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

with open("starter-data.json", "r") as fp:
    employees = json.load(fp)

class Employees(Resource):

    def get(self):
        return employees

api.add_resource(Employees, "/")

# @app.route("/")
# def index():
#     return jsonify(employees)

if __name__ == "__main__":
    app.run(debug=True)