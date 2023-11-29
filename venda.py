import mysql.connector
from datetime import datetime

class Venda:
    def __init__(self, conn, cliente_id):
        self.conn = conn
        self.cliente_id = cliente_id
        self.data = datetime.now()
        self.total = 0
        self.itens = []  # Lista para armazenar os itens da venda

        # Criar uma nova venda no banco de dados
        self.id = self._criar_nova_venda()

    def _criar_nova_venda(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("INSERT INTO Vendas (data, total, cliente_id) VALUES (%s, %s, %s)", (self.data, self.total, self.cliente_id))
            self.conn.commit()
            venda_id = cursor.lastrowid
            return venda_id
        except mysql.connector.Error as err:
            print(f"Erro ao criar nova venda: {err}")
        finally:
            if 'cursor' in locals():
                cursor.close()

    def adicionar_item(self, produto_id, quantidade):
        try:
            cursor = self.conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM Produtos WHERE id = %s", (produto_id,))
            produto = cursor.fetchone()

            if produto:
                subtotal = produto['preco'] * quantidade
                self.itens.append({'produto_id': produto_id, 'quantidade': quantidade, 'subtotal': subtotal})
                self.total += subtotal
                print(f"Item adicionado à venda: {produto['nome']} (Quantidade: {quantidade}, Subtotal: {subtotal})")
            else:
                print("Produto não encontrado.")
        except mysql.connector.Error as err:
            print(f"Erro ao adicionar item à venda: {err}")
        finally:
            if 'cursor' in locals():
                cursor.close()

    def finalizar_venda(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("UPDATE Vendas SET total = %s WHERE id = %s", (self.total, self.id))
            self.conn.commit()
            print(f"Venda finalizada. Total da venda: {self.total}")
        except mysql.connector.Error as err:
            print(f"Erro ao finalizar venda: {err}")
        finally:
            if 'cursor' in locals():
                cursor.close()

    def gerar_relatorio(self):
        try:
            cursor = self.conn.cursor(dictionary=True)
            cursor.execute("""
                SELECT Vendas.id AS venda_id, Vendas.data, Vendas.total,
                    Clientes.id AS cliente_id, Clientes.nome AS cliente_nome,
                    Produtos.id AS produto_id, Produtos.nome AS produto_nome,
                    ItensVenda.quantidade, ItensVenda.subtotal
                FROM Vendas
                JOIN Clientes ON Vendas.cliente_id = Clientes.id
                JOIN ItensVenda ON Vendas.id = ItensVenda.id_venda
                JOIN Produtos ON ItensVenda.id_produto = Produtos.id
                WHERE Vendas.id = %s
            """, (self.id,))
            
            vendas_info = cursor.fetchall()

            if vendas_info:
                venda = vendas_info[0]  # Assume que todas as linhas pertencem à mesma venda

                print(f"Relatório de Venda (ID: {venda['venda_id']}, Cliente ID: {venda['cliente_id']}, "
                    f"Cliente: {venda['cliente_nome']}, Data: {venda['data']}, Total: {venda['total']})")

                for item in vendas_info:
                    print(f"  Produto ID: {item['produto_id']}, Produto: {item['produto_nome']}, "
                        f"Quantidade: {item['quantidade']}, Subtotal: {item['subtotal']}")
            else:
                print("Nenhum item encontrado para esta venda.")
        except mysql.connector.Error as err:
            print(f"Erro ao gerar relatório de venda: {err}")
        finally:
            if 'cursor' in locals():
                cursor.close()

