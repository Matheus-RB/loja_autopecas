class Produto:
    def __init__(self, nome, preco, quantidade):
        self.__nome = nome
        self.__preco = preco
        self.__quantidade = quantidade
    
    def obter_dados(self):
        return self.__nome, self.__preco, self.__quantidade

    def __str__(self):
        return f"Produto(nome={self.__nome}, preco={self.__preco}), quantidade={self.__quantidade}"
