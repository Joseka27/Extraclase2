from flask import Flask
from flask_cors import CORS
from controller.user_controller import user_blueprint

# Crear una instancia de la aplicación Flask
app = Flask(__name__)
CORS(app)  # Configurar CORS para permitir todas las solicitudes

# Registrar el blueprint de usuario
app.register_blueprint(user_blueprint, url_prefix='/user')

if __name__ == '__main__':
    app.run(port=5000)
