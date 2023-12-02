class Venda:
    def __init__(self, cliente_id, data, total = 0):
        self.__cliente_id = cliente_id
        self.__data = data
        self.__total = total

    def obter_dados(self):
        return self.__data, self.__total, self.__cliente_id
    
    def __str__(self):
        return f"Venda(cliente_id={self.__cliente_id}, data={self.__data}, total={self.__total})"
