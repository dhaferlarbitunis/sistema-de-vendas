class Produto:

    def __init__(self, ProdutoID=None, nome="", descricao="", preco=0.0, quantidadeEstoque=0):
        self.__ProdutoID = ProdutoID
        self.__nome = nome
        self.__descricao = descricao
        self.__preco = preco
        self.__quantidadeEstoque = quantidadeEstoque

    @property
    def ProdutoID(self):
        return self.__ProdutoID

    @property
    def nome(self):
        return self.__nome

    @property
    def descricao(self):
        return self.__descricao

    @property
    def preco(self):
        return self.__preco

    @property
    def quantidadeEstoque(self):
        return self.__quantidadeEstoque
