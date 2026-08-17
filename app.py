from flask import Flask, send_file
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# ТВОЙ КОНФИГ (замени ключи!)
CONFIG = """[Interface]
PrivateKey = ТВОЙ_ПРИВАТНЫЙ_КЛЮЧ_СЕРВЕРА
Address = 10.0.0.1/24
ListenPort = 51820

[Peer]
PublicKey = ПУБЛИЧНЫЙ_КЛЮЧ_КЛИЕНТА
AllowedIPs = 10.0.0.2/32
"""

@app.route('/')
def index():
    return {"status": "online", "service": "Черепашка VPN"}

@app.route('/config')
def get_config():
    return CONFIG, 200, {'Content-Type': 'text/plain'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
