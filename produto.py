class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def __str__(self):
        return f"Produto(nome={self.nome}, preco={self.preco}), quantidade={self.quantidade}"
