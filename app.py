from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return "Servidor activo. Usa /get-euro para el dato."

@app.route('/get-euro')
def get_euro():
    try:
        url = "https://query1.finance.yahoo.com/v8/finance/chart/EURCOP=X"
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, verify=False)
        data = response.json()
        precio = data['chart']['result'][0]['meta']['regularMarketPrice']
        return jsonify({"status": "success", "valor": precio})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run()
