from flask import Flask, jsonify, request
from clienteRepository import ClienteRepository

app = Flask(__name__)

@app.route("/clientes", methods=['GET'])
def listar_clientes():
    repo = ClienteRepository()
    dados = repo.find_all()

    cabecalhos = ["ClienteID","nome", "cpf", "email", "Telefone", "Endereco", "Cidade", "Estado", "CEP"]
    dados_retorno = [dict(zip(cabecalhos, d)) for d in dados]

    return jsonify(dados_retorno)

@app.route("/clientes", methods=['POST'])
def cadastrar_produto():
    repo = ClienteRepository()
    dados = request.get_json()

    repo.create(
        dados.get("nome"),
        dados.get("cpf"),
        dados.get("email"),
        dados.get("Telefone"),
        dados.get("Endereco"),
        dados.get("Cidade"),
        dados.get("Estado"),
        dados.get("Cep")
    )

    return jsonify({"mensagem": "Cliente cadastrado com sucesso"}), 201

@app.route("/clientes/<int:cliente_id>", methods=['DELETE'])
def remover_cliente(cliente_id):
    repo = ProdutoRepository()
    repo.delete(cliente_id)
    return jsonify({"mensagem": "Cliente removido com sucesso"})

if __name__ == "__main__":
    app.run(debug=True)
