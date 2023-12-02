class ItemVenda:
    def __init__(self, id_produto, quantidade, id_venda):
        self.__quantidade = quantidade
        self.__id_produto = id_produto
        self.__id_venda = id_venda

    def obter_dados(self):
        return self.__quantidade, self.__id_produto, self.__id_venda
    
    def __str__(self):
        return f"ItemVenda(id_produto={self.__id_produto}, quantidade={self.__quantidade}, id_venda={self.__id_venda})"