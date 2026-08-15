from fastapi import FastAPI
from fastapi.responses import FileResponse
import random
import string
import hashlib
from datetime import datetime

app = FastAPI(title="Черепашка VPN API")

@app.get("/")
def root():
    return {"service": "Черепашка VPN", "status": "online"}

@app.get("/config")
def get_config():
    private_key = ''.join(random.choices(string.ascii_letters + string.digits + '+/=', k=44))
    public_key = ''.join(random.choices(string.ascii_letters + string.digits + '+/=', k=44))
    
    config = f"""[Interface]
PrivateKey = {private_key}
Address = 10.0.0.2/32
DNS = 1.1.1.1, 8.8.8.8
MTU = 1280

[Peer]
PublicKey = {public_key}
Endpoint = engage.cloudflareclient.com:2408
AllowedIPs = 0.0.0.0/0
PersistentKeepalive = 25

# 🐢 ЧЕРЕПАШКА VPN
# Сгенерировано автоматически
# Безлимитный трафик
"""
    
    filename = f"config_{datetime.now().strftime('%Y%m%d%H%M%S')}.conf"
    with open(filename, 'w') as f:
        f.write(config)
    
    return FileResponse(filename, filename=filename)