from flask import Flask, request, jsonify
app = Flask(__name__)
from apisback import weather_bp

from flask_cors import CORS
CORS(app)

app.register_blueprint(weather_bp)

@app.route('/')
def index():
    return 'Hello, Flask!'


if __name__ == '__main__':
    app.run(debug=True)

#Podés tener un input donde el usuario elija:

#Detectar ubicación automáticamente (geolocalización)

#Escribir nombre de ciudad

#Escribir código postal

#Y en función de lo que complete, armar la URL de la API.