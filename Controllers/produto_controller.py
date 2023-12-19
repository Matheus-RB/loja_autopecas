from Models.database import Database
from Models.produto import Produto

class ProdutoController:
    def __init__(self):
        self.db = Database()

    def adicionar_produto(self, nome, preco, quantidade):
        produto = Produto(nome, preco, quantidade)
        query = "INSERT INTO produtos (nome, preco, quantidade) VALUES (%s, %s, %s)"
        values = (produto.nome, produto.preco, produto.quantidade)
        self.db.cursor.execute(query, values)
        self.db.conn.commit()
