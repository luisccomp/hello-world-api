from flask import Blueprint

routes = Blueprint('welcome', __name__)


@routes.route('/api/welcome', methods=['GET'])
def welcome():
    return { 'message': 'Hello World' }