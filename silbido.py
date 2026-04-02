cat <<EOF > silbido.py
import requests
import time
import os

archivo_urls = "urls.txt"

def martillo_pilon(url_objetivo, repeticiones=30):
    dominio = url_objetivo.split('/')[2]
    key = "777silbido77766655544433322211100" 
    
    motores = ["https://www.bing.com/indexnow", "https://yandex.com/indexnow"]

    for i in range(repeticiones):
        print(f"🔨 Golpe {i+1}/30 para {url_objetivo}...")
        
        data = {
            "host": dominio,
            "key": key,
            "keyLocation": f"https://{dominio}/{key}.txt",
            "urlList": [url_objetivo]
        }

        for motor in motores:
            try:
                r = requests.post(motor, json=data, timeout=10)
                print(f"   🛰️ {motor.split('.')[1].upper()}: Estado {r.status_code}")
            except:
                print(f"   ❌ Error en motor {motor}")
        
        time.sleep(2) 

if os.path.exists(archivo_urls):
    with open(archivo_urls, "r") as f:
        urls = [line.strip() for line in f if line.strip()]
        for u in urls:
            martillo_pilon(u)
EOF