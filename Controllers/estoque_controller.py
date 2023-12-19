from Models.database import Database

class EstoqueController:
    def __init__(self):
        self.db = Database()

    def consultar_estoque(self):
        query = "SELECT id, nome, quantidade FROM produtos"
        self.db.cursor.execute(query)
        estoque = self.db.cursor.fetchall()
        return estoque
