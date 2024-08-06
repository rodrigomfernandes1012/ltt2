from flask import Flask, request, jsonify,  render_template, url_for, request, redirect, flash
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)


#atudir
@app.route('/')
def index():
    return render_template("index.html")



@app.route('/submit', methods=['POST'])
def submit_data():
    data = request.json
    name = data.get('name')
    phone = data.get('phone')
    payment_method = data.get('payment_method')

    data_dict = {
        "name": name,
        "phone": phone,
        "payment_method": payment_method
    }

    # Aqui você pode processar ou armazenar o dicionário como necessário
    print(data_dict)
    #return render_template("index.html")
    return jsonify({"message": "Obrigado por solicitar o Táxi", "data": data_dict})


def main():
   # port = int(os.environ.get("PORT", 8080))
   # app.run(host="127.0.0.1", port=port)
    port = int(os.environ.get("PORT", 80))
    app.run(host="192.168.15.200", port=port)


if __name__ == "__main__":
    main()


