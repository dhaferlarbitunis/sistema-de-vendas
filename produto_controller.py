from flask import Flask,Blueprint, jsonify, request
from ProdutoRepository import ProdutoRepository
from produto import Produto

produto_bp = Blueprint("produto". __name__)

@produto_bp.route("/produtos", methods=['GET'])
def listar_produtos():
    repo = ProdutoRepository()
    dados = repo.find_all()

    cabecalhos = ["ProdutoID", "nome", "descricao", "preco", "quantidadeEstoque"]
    dados_retorno = [dict(zip(cabecalhos, d)) for d in dados]

    return jsonify(dados_retorno)

@produto_bp.route("/produtos", methods=['POST'])
def cadastrar_produto():
    repo = ProdutoRepository()
    dados = request.get_json()

    repo.create(
        dados.get("nome"),
        dados.get("descricao"),
        dados.get("preco"),
        dados.get("quantidadeEstoque")
    )

    return jsonify({"mensagem": "Produto cadastrado com sucesso"}), 201

@produto_bp.route("/produtos/<int:produto_id>", methods=['DELETE'])
def remover_produto(produto_id):
    repo = ProdutoRepository()
    repo.delete(produto_id)
    return jsonify({"mensagem": "Produto removido com sucesso"})

