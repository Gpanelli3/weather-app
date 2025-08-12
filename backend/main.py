from flask import Flask, request, jsonify
app = Flask(__name__)
from weather import weather_bp
from fiveDays import fiveDays

from flask_cors import CORS
CORS(app)

app.register_blueprint(weather_bp)
app.register_blueprint(fiveDays)

@app.route('/')
def index():
    return 'CLIMA 24/7'


if __name__ == '__main__':
    app.run(debug=True)
