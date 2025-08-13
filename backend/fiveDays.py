from flask import request, jsonify, Blueprint
import requests

fiveDays_bp = Blueprint('fiveDays', __name__, url_prefix='/fiveDays')

@fiveDays_bp.route('/', methods=['POST', 'OPTIONS'])
def five_days():
    if request.method == 'OPTIONS':
        return jsonify({'ok': True}), 200
    data = request.get_json()
    ciudad = data.get("ciudad", "")

    api_key = "74a499c84c5ab588fb5b24eb0a9214bc"
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={ciudad}&appid={api_key}&units=metric&lang=es'

    respuesta = requests.get(url)
    
    if respuesta.status_code == 200:
        datos = respuesta.json()
        pronostico = []
        # Tomar un dato cada 8 (24 horas) para aproximar un día
        for i in range(0, min(40, len(datos["list"])), 8):
            dia = datos["list"][i]
            pronostico.append({
                "fecha": dia["dt_txt"],
                "temperatura": dia["main"]["temp"],
                "descripcion": dia["weather"][0]["description"],
            })
        resultado = {
            "ciudad": datos["city"]["name"],
            "pronostico": pronostico
        }
        return jsonify(resultado)
    else:
        return jsonify({"error": "No se pudo obtener el clima"}), 400