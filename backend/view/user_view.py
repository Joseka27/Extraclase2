from flask import jsonify

def user_response(tema):
    response = {
        'status': 'success',
        'user': {
            'nombre': tema.nombre,
            'comentario': tema.comentario
        }
    }
    return jsonify(response)
