import requests
import time
import os

archivo_urls = "urls.txt"

def martillo_pilon(url_objetivo, repeticiones=30):
    # Extraemos el dominio de la URL (ej: azaguirreramarfp-web.github.io)
    dominio = url_objetivo.split('/')[2]
    # Esta es tu clave de identificación ante los buscadores
    key = "777silbido77766655544433322211100" 
    
    motores = ["https://www.bing.com/indexnow", "https://yandex.com/indexnow"]

    print(f"🚀 Iniciando secuencia de 30 pings para: {url_objetivo}")

    for i in range(repeticiones):
        print(f"🔨 Golpe {i+1}/30...")
        
        data = {
            "host": dominio,
            "key": key,
            "keyLocation": f"https://{dominio}/{key}.txt",
            "urlList": [url_objetivo]
        }

        for motor in motores:
            try:
                # Enviamos la señal a Bing/Yandex
                r = requests.post(motor, json=data, timeout=10)
                nombre_motor = "BING" if "bing" in motor else "YANDEX"
                print(f"   🛰️ {nombre_motor}: Estado {r.status_code}")
            except:
                print(f"   ❌ Error conectando con {motor}")
        
        # Pausa de 2 segundos para no parecer un ataque y que no nos bloqueen
        time.sleep(2) 

    print("✅ Misión cumplida: 30 pings enviados.")

# Ejecución principal: Lee el archivo urls.txt y lanza el martillo
if os.path.exists(archivo_urls):
    with open(archivo_urls, "r") as f:
        urls = [line.strip() for line in f if line.strip()]
        if not urls:
            print("⚠️ El archivo urls.txt está vacío.")
        for u in urls:
            martillo_pilon(u)
else:
    print(f"❌ No se encuentra el archivo {archivo_urls}")
