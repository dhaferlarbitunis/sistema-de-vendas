from flask import Flask, jsonify
import requests


endereco = Flask(__name__)

@endereco.route("/<cep>")
def get_endereco(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    #ira fazer
    dados_endereco = requests.get(url)
    endereco_json = dados_endereco.json()
    #return {"messagem":f"endereco {cep} encontrado con sucesso"}
    rua = endereco_json.get("logradouro")
    cidade = endereco_json.get("localidade")
    estado = endereco_json.get("estado")

    endereco_retorno = {
        "messagem": "Endereco encontrado com sucesso",
        "rua": rua,
        "cidade": cidade,
        "estado":estado
    }
    return jsonify(endereco_retorno)

if __name__ == "__main__":
    endereco.run(debug=True, port=8080)