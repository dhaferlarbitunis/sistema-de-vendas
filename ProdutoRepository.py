from conexao import Conexao

class ProdutoRepository:

    def __init__(self):
        self.conexao = Conexao()

    def find_all(self):
        cursor = self.conexao.get_cursor()
        cursor.execute("""
            SELECT 
                ProdutoID,
                Nome,
                Descricao,
                Preco,
                QuantidadeEstoque
            FROM Produto
            ORDER BY ProdutoID
        """)
        return cursor.fetchall()

    def create(self, nome, descricao, preco, quantidadeEstoque):
        cursor = None
        try:
            cursor = self.conexao.get_cursor()
            cursor.execute("""
                INSERT INTO Produto (Nome, Descricao, Preco, QuantidadeEstoque)
                VALUES (%s, %s, %s, %s)
            """, (nome, descricao, preco, quantidadeEstoque))
            self.conexao.get_conexao().commit()
            return cursor.lastrowid
        except Exception as e:
            print("Erro ao criar produto:", e)
            self.conexao.get_conexao().rollback()
            return None
        finally:
            if cursor:
                cursor.close()

    def delete(self, produto_id):
        cursor = None
        try:
            cursor = self.conexao.get_cursor()
            cursor.execute(
                "DELETE FROM Produto WHERE ProdutoID = %s",
                (produto_id,)
            )
            self.conexao.get_conexao().commit()
            return cursor.rowcount > 0
        except Exception as e:
            print("Erro ao deletar produto:", e)
            self.conexao.get_conexao().rollback()
            return False
        finally:
            if cursor:
                cursor.close()
