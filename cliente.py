class Cliente:
    def __init__(self, nome, telefone, endereco):
        self.__nome = nome
        self.__telefone = telefone
        self.__endereco = endereco

    def obter_dados_para_banco(self):
        return self.__nome, self.__telefone, self.__endereco

    def __str__(self):
        return f"Cliente(nome={self.__nome}, telefone={self.__telefone}), endereco={self.__endereco}"
