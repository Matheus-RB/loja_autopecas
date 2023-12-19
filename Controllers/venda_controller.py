from Models.database import Database
from Models.venda import Venda

class VendaController:
    def __init__(self):
        self.db = Database()

    def realizar_venda(self, cliente_id, id_produto, quantidade):
        from datetime import date
        data = date.today()

        query_produto = "SELECT preco, quantidade FROM produtos WHERE id = %s"
        values_produto = (id_produto,)
        self.db.cursor.execute(query_produto, values_produto)
        result = self.db.cursor.fetchone()

        if result:
            preco, quantidade_disponivel = result
            
            quantidade = int(quantidade)
            quantidade_disponivel = int(quantidade_disponivel)

            if quantidade <= quantidade_disponivel:
                total = quantidade * preco

                venda = Venda(data, total, cliente_id)
                query_venda = "INSERT INTO vendas (data, total, cliente_id) VALUES (%s, %s, %s)"
                values_venda = (venda.data, venda.total, venda.cliente_id)
                self.db.cursor.execute(query_venda, values_venda)
                venda_id = self.db.cursor.lastrowid
                self.db.conn.commit()

                query_item = "INSERT INTO itens_vendas (id_venda, id_produto, quantidade, subtotal) VALUES (%s, %s, %s, %s)"
                subtotal = quantidade * preco
                values_item = (venda_id, id_produto, quantidade, subtotal)
                self.db.cursor.execute(query_item, values_item)
                self.db.conn.commit()

                nova_quantidade = quantidade_disponivel - quantidade
                query_atualizar_estoque = "UPDATE produtos SET quantidade = %s WHERE id = %s"
                values_atualizar_estoque = (nova_quantidade, id_produto)
                self.db.cursor.execute(query_atualizar_estoque, values_atualizar_estoque)
                self.db.conn.commit()

                return venda_id
            else:
                print("Quantidade insuficiente em estoque.")
        else:
            print("Produto não encontrado.")
