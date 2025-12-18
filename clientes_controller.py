from flask import Flask, jsonify
from conexao import Conexao

app = Flask(__name__)

@app.route("/cliente/<cpf>")
def get_cliente(cpf):
    conexao = Conexao()
    cursor = conexao.get_cursor()

    sql = """
        SELECT Nome, CPF, Cidade, Estado
        FROM Cliente
        WHERE CPF = %s
    """
    cursor.execute(sql, (cpf,))
    cliente = cursor.fetchone()



  

    if not cliente:
        return jsonify({"mensagem": "Cliente não encontrado"}), 404
    
    # conexao.fechar_conexao()
    return jsonify({
        "mensagem": "Cliente encontrado com sucesso",
        "nome": cliente[0],     
        "cpf": cliente[1],      
        "cidade": cliente[2],   
        "estado": cliente[3]    
    }), 200


if __name__ == "__main__":
    app.run(debug=True, port=8080)
