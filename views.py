from flask import Blueprint, request, jsonify

api = Blueprint('api', 'api', url_prefix='/api')


@api.route('/')
def hello():
    return "Hello World!"


@api.route('/<name>')
def hello_name(name):
    return jsonify(name=name, message='OK')
