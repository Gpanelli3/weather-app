from flask import Flask, request, jsonify, Blueprint
import requests

weather_bp = Blueprint('weather', __name__, url_prefix='/weather')

@weather_bp.route('/clima')
def clima():
    ciudad = request.json('ciudad')  # Valor por defecto si no se proporcion
    api_key = "74a499c84c5ab588fb5b24eb0a9214bc"  # Reemplaza con tu clave real
    url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric&lang=es"
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        datos = respuesta.json()
        resultado = {
            "ciudad": datos["name"],
            "temperatura": datos["main"]["temp"],
            "descripcion": datos["weather"][0]["description"],
        }
        print(datos)
        return jsonify(resultado)
    else:
        return jsonify({"error": "No se pudo obtener el clima"}), 400

