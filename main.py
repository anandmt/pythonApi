from flask import Flask, jsonify
from flask_restful import Api
from helloworld import HelloWorld

app = Flask(__name__)
api = Api(app)

api.add_resource(HelloWorld, "/hello/<string:name>/<int:age>")


@app.route('/')
def hello_world():
    return jsonify(message="hello world"), 200


if __name__ == '__main__':
    app.run(debug=True)
