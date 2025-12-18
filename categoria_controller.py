from flask import Flask, jsonify, request, Blueprint
from categoriaRepository import CategoriaRepository
from categoria import Categoria



categoria_bp = Blueprint("categoria", __name__)
@categoria_bp.route("/ola", methods = ['GET'])
def ola():
    return "minha primeira API"

@categoria_bp.route("/clientes", methods = ['Get'])
def listar_clientes():
    dados = [{"nome": "Leonado"}, {"nome":"Maria"}, {"nome":"Silvo"}, {"nome":"Dhafer"}]
    return jsonify(dados)

@categoria_bp.route("/categorias", methods = ['GET'])
def listar_categorias():
    #dados = [{}]
    #repo = CategoriaRepository()
    #dados =  repo.find_all()
    #return dados
    repo = CategoriaRepository()
    dados = repo.find_all()

      #dados = [
       # {
        #    "id": categoria[0],
         #   "nome": categoria[1],
          #  "descricao": categoria[2]
        #}
        #for categoria in categorias
    #]
    cabecalhos = ["id", "nome", "descricao"]
    dados_retorno = [dict(zip(cabecalhos, d)) for d in dados]
    return jsonify(dados_retorno)

@categoria_bp.route("/categorias/<int:categoriaID>")
def buscar_por_id(categoriaID):
    repo = CategoriaRepository()
    categoria = repo.find_by_id(categoriaID)
    categoria_retorno = {"id": categoria[0], "nome": categoria[1], "descricao": categoria[2]}
    return jsonify(categoria_retorno)

@categoria_bp.route("/categorias", methods =['POST'])
def cadastrar_categoria():
    repo = CategoriaRepository()
    dados_json = request.get_json()

    id = dados_json.get("id")
    nome = dados_json.get("nome")
    descricao = dados_json.get("descricao")
    #enviando para a banco de dados

    repo.create(nome, descricao)
    return jsonify({
    'messagem': 'Categorias cadastrar com sucesso',
    'nome': nome,
    'descricao': descricao
   
   }), 201

@categoria_bp.route("/categorias/<int:id_categiria>", methods=['DELETE'])
def remove_categoria(id_categiria):
    #objeto de comunicacao com banco de dados
    repo = CategoriaRepository()
    #removendo a categoria do banco de dados
    repo.delete(id_categiria)
    return jsonify(
        {
        "messagem": "Categoria remivida com sucesso"
        }
    )



