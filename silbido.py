import requests
import json
import os

# Archivo donde guardarás las URLs que quieres indexar (una por línea)
archivo_urls = "urls.txt"

def mandar_ping(url_objetivo):
    # El protocolo IndexNow pide un Host y una Key
    dominio = url_objetivo.split('/')[2]
    # Usamos una clave fija para que los buscadores nos reconozcan
    key = "777silbido77766655544433322211100" 

    data = {
        "host": dominio,
        "key": key,
        "keyLocation": f"https://{dominio}/{key}.txt",
        "urlList": [url_objetivo]
    }

    motores = ["https://www.bing.com/indexnow", "https://yandex.com/indexnow"]
    
    for motor in motores:
        try:
            r = requests.post(motor, json=data, timeout=10)
            print(f"🛰️ Ping a {motor} para {url_objetivo}: Estado {r.status_code}")
        except:
            print(f"❌ Error conectando con {motor}")

if os.path.exists(archivo_urls):
    with open(archivo_urls, "r") as f:
        urls = [line.strip() for line in f if line.strip()]
        for u in urls:
            mandar_ping(u)
