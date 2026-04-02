import requests
import time
import os

archivo_urls = "urls.txt"

def martillo_pilon(url_objetivo, repeticiones=30):
    dominio = url_objetivo.split('/')[2]
    key = "777silbido77766655544433322211100" 
    motores = ["https://www.bing.com/indexnow", "https://yandex.com/indexnow"]
    print(f"🚀 Iniciando 30 pings para: {url_objetivo}")
    for i in range(repeticiones):
        print(f"🔨 Golpe {i+1}/30...")
        data = {"host": dominio, "key": key, "keyLocation": f"https://{dominio}/{key}.txt", "urlList": [url_objetivo]}
        for motor in motores:
            try:
                requests.post(motor, json=data, timeout=10)
            except:
                pass
        time.sleep(2) 
    print("✅ Misión cumplida.")

if os.path.exists(archivo_urls):
    with open(archivo_urls, "r") as f:
        for u in [line.strip() for line in f if line.strip()]:
            martillo_pilon(u)
