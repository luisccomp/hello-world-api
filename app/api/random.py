from random import randint
from flask import Blueprint

routes = Blueprint('random', __name__)

@routes.route('/api/random', methods=['GET'])
def random():
    return { 'number': randint(0, 100) }
