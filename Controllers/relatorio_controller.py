from Models.database import Database

class RelatorioController:
    def __init__(self):
        self.db = Database()

    def obter_relatorio_vendas(self):
        query = """
        SELECT vendas.id, vendas.data, vendas.total, clientes.nome as cliente_nome
        FROM vendas
        JOIN clientes ON vendas.cliente_id = clientes.id
        """
        self.db.cursor.execute(query)
        vendas = self.db.cursor.fetchall()
        return vendas
