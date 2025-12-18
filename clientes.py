class Clientes:

    def __init__(self, ClienteID=None, nome="", cpf="", email="", Telefone="", Endereco= "", Cidadde = "", Estado = "", CEP=""):
        self.__ClienteID = ClienteID
        self.__nome = nome
        self.__cpf = cpf
        self.__email = email
        self.__Telefone = Telefone
        self.__Endereco = Endereco
        self.__Cidadde = Cidade
        self.__Estado = Estado
        self.__CEP = CEP

    @property
    def ClienteID(self):
        return self.__ClienteID

    @property
    def nome(self):
        return self.__nome

    @property
    def cpf(self):
        return self.__cpf

    @property
    def email(self):
        return self.__email

    @property
    def Telefone(self):
        return self.__Telefone

    @property
    def Cidadde(self):
        return self.__Cidade

    @property
    def Estado(self):
        return self.__Estado

    @property
    def Cep(self):
        return self.__Cep



