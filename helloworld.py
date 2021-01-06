from flask import jsonify
from flask_restful import Resource


class HelloWorld(Resource):
    def get(self, name, age):
        return jsonify(data=f"Hello World {name}, your age is {age}")

    def user_details(self, name, age):
        return jsonify(data=f"Hello World {name}, your age is {age}")

    def post(self):
        return jsonify(data="posted")