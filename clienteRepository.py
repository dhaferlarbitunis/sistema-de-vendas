from conexao import Conexao

class ClienteRepository:

    def __init__(self):
        self.conexao = Conexao()

    def find_all(self):
        cursor = self.conexao.get_cursor()
        cursor.execute("""
            SELECT 
                ClienteID,
                Nome,
                cpf,
                email,
                Telefone,
                Endereco,
                Cidade,
                Estado,
                Cep
            FROM Cliente
            ORDER BY ClienteID
        """)

        return cursor.fetchall()

    def create(self,  nome, cpf, email, Telefone, Endereco, Cidade, Estado, CEP):
        cursor = None
        try:
            cursor = self.conexao.get_cursor()
            cursor.execute("""
                INSERT INTO Cliente ( nome, cpf, email, Telefone, Endereco, Cidade, Estado, CEP)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, ( nome, cpf, email, Telefone, Endereco, Cidade, Estado, CEP))
            self.conexao.get_conexao().commit()
            return cursor.lastrowid
        except Exception as e:
            print("Erro ao criar Cliente:", e)
            self.conexao.get_conexao().rollback()
            return None
        finally:
            if cursor:
                cursor.close()

    def delete(self, cliente_id):
        cursor = None
        try:
            cursor = self.conexao.get_cursor()
            cursor.execute(
                "DELETE FROM Produto WHERE ClienteID = %s",
                (cliente_id,)
            )
            self.conexao.get_conexao().commit()
            return cursor.rowcount > 0
        except Exception as e:
            print("Erro ao deletar Cliente:", e)
            self.conexao.get_conexao().rollback()
            return False
        finally:
            if cursor:
                cursor.close()
