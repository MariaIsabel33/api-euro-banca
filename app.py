import requests
from datetime import datetime

def consultar_euro_yahoo():
    # URL de Yahoo Finance para Euro a Peso Colombiano
    # Esta es una de las fuentes más estables del mundo
    url = "https://query1.finance.yahoo.com/v8/finance/chart/EURCOP=X"
    
    # Headers para que parezca una consulta de navegador normal
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    try:
        print("Conectando con Yahoo Finance...")
        response = requests.get(url, headers=headers)
        data = response.json()

        # Navegamos por el JSON de Yahoo para llegar al precio actual
        precio = data['chart']['result'][0]['meta']['regularMarketPrice']
        
        # ... (dentro de tu función después de obtener el precio)
        ahora = datetime.now().strftime("%d/%m/%Y %I:%M:%S %p")
        print(f"\n*******************************")
        print(f"   VALOR DEL EURO (VERIFICADO) ")
        print(f"   Precio: $ {precio} COP")
        print(f"   Fecha: {ahora}")
        print(f"   Fuente: Yahoo Finance Real-Time")
        print(f"*******************************\n")
        
    except Exception as e:
        print(f"Incluso Yahoo falló. Error: {e}")
        print("Si ves este error, es muy probable que el Firewall de tu empresa esté bloqueando Python.")

consultar_euro_yahoo()