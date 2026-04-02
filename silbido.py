cat <<EOF > silbido.py
import requests
import time
import os
archivo_urls = "urls.txt"
def martillo_pilon(url_objetivo, repeticiones=30):
    dominio = url_objetivo.split('/')[2]
    key = "777silbido77766655544433322211100"
    motores = ["https://www.bing.com/indexnow"]
    print(f"🚀 INICIANDO ATAQUE DE 30 PINGS...")
    for i in range(repeticiones):
        print(f"🔨 GOLPE {i+1}/30 a las {time.strftime('%H:%M:%S')}")
        data = {"host": dominio, "key": key, "keyLocation": f"https://{dominio}/{key}.txt", "urlList": [url_objetivo]}
        try:
            requests.post(motores[0], json=data, timeout=10)
        except:
            pass
        time.sleep(2)
    print("✅ FIN DEL MARTILLO.")

if os.path.exists(archivo_urls):
    with open(archivo_urls, "r") as f:
        for u in [line.strip() for line in f if line.strip()]:
            martillo_pilon(u)
EOF