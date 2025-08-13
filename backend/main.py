from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
from weather import weather_bp
from fiveDays import fiveDays_bp

CORS(app, origins=["http://localhost:3000"], supports_credentials=True, allow_headers="*", methods=["GET", "POST", "OPTIONS"])

app.register_blueprint(weather_bp)
app.register_blueprint(fiveDays_bp)

@app.route('/')
def index():
    return 'CLIMA 24/7'


if __name__ == '__main__':
    app.run(debug=True)
