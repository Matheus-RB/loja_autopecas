from Models.database import Database
from Models.cliente import Cliente

class ClienteController:
    def __init__(self):
        self.db = Database()

    def adicionar_cliente(self, nome, telefone, endereco):
        cliente = Cliente(nome, telefone, endereco)
        query = "INSERT INTO clientes (nome, telefone, endereco) VALUES (%s, %s, %s)"
        values = (cliente.nome, cliente.telefone, cliente.endereco)
        self.db.cursor.execute(query, values)
        self.db.conn.commit()
