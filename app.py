import json
import pandas as pd
from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse

JSON_FILE = "starter-data.json"

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('employee', type=dict, required=True)

def readFile(JSON_FILE):
    with open(JSON_FILE, "r") as fp:
        data = json.load(fp)
    return data["employees"]

def updateFile(JSON_FILE, data):
    with open(JSON_FILE, 'w') as fp:
        json.dump({ "employees": data }, fp)

class Employees(Resource):

    def get(self):
        data = readFile(JSON_FILE)
        dataFrame = pd.DataFrame.from_dict(data)
        response = dataFrame.to_dict("records")
        return response, 200

    def post(self):
        data = readFile(JSON_FILE)
        args = parser.parse_args()
        body = args["employee"]

        #Create datatframe and append new employee object
        dataFrame = pd.DataFrame.from_dict(data)
        dataFrame = dataFrame.append(body, ignore_index=True)

        #Write update data to file
        response = dataFrame.to_dict("records")
        updateFile(JSON_FILE, response)

        return response, 200

class Employee(Resource):

    def get(self, name):
        data = readFile(JSON_FILE)
        for e in data:
            if e["name"].lower() == name.lower():
                match = e
            else:
                match = {}
        return match, 200

api.add_resource(Employee, "/employee", "/employee/<name>")
api.add_resource(Employees, "/", "/employees")


if __name__ == "__main__":
    app.run(debug=True)