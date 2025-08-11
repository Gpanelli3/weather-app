from flask import Flask, request, jsonify
import requests
app = Flask(__name__)

from flask_cors import CORS
CORS(app)

@app.route('/')
def index():
    return 'Hello, Flask!'

@app.route('/clima')
def clima():
    ciudad = request.args.get('ciudad', default='Buenos Aires')
    api_key = "74a499c84c5ab588fb5b24eb0a9214bc"  # Reemplaza con tu clave real
    url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric&lang=es"
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        datos = respuesta.json()
        resultado = {
            "ciudad": datos["name"],
            "temperatura": datos["main"]["temp"],
            "descripcion": datos["weather"][0]["description"],
            "humedad": datos["main"]["humidity"]
        }
        return jsonify(resultado)
    else:
        return jsonify({"error": "No se pudo obtener el clima"}), 400

if __name__ == '__main__':
    app.run(debug=True)

#Podés tener un input donde el usuario elija:

#Detectar ubicación automáticamente (geolocalización)

#Escribir nombre de ciudad

#Escribir código postal

#Y en función de lo que complete, armar la URL de la API.