from flask import Blueprint, request, jsonify
from services.user_service import UserService

user_blueprint = Blueprint('user', __name__)
user_service = UserService()

@user_blueprint.route('/submit', methods=['POST'])
def submit():
    data = request.json
    tema = data.get('tema')
    nombre = data.get('nombre')
    comentario = data.get('comentario')

    if not nombre or not comentario or not tema:
        return jsonify({'error': 'Missing required fields'}), 400

    user = user_service.create_user(tema, nombre, comentario)
    return jsonify(user.serialize()), 201

@user_blueprint.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = user_service.get_user(user_id)
    if user:
        return jsonify(user.serialize())
    else:
        return jsonify({'error': 'User not found'}), 404