import mysql.connector

class Database:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
        )
        self.cursor = self.conn.cursor()

        self.create_database()

        self.conn.database = 'loja_autopecas'

        self.create_tables()

    def create_database(self):
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS loja_autopecas")
        self.conn.commit()

    def create_tables(self):
        clients_query = """
        CREATE TABLE IF NOT EXISTS clientes (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(255),
            telefone VARCHAR(20),
            endereco VARCHAR(50)
        )
        """
        self.cursor.execute(clients_query)

        products_query = """
        CREATE TABLE IF NOT EXISTS produtos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(255),
            preco DECIMAL(10, 2),
            quantidade INT
        )
        """
        self.cursor.execute(products_query)

        sales_query = """
        CREATE TABLE IF NOT EXISTS vendas (
            id INT AUTO_INCREMENT PRIMARY KEY,
            data DATE,
            total DECIMAL(10, 2),
            cliente_id INT,
            FOREIGN KEY (cliente_id) REFERENCES clientes(id)
        )
        """
        self.cursor.execute(sales_query)

        items_query = """
        CREATE TABLE IF NOT EXISTS itens_vendas (
            id INT AUTO_INCREMENT PRIMARY KEY,
            id_produto INT,
            id_venda INT,
            quantidade INT,
            subtotal DECIMAL(10, 2),
            FOREIGN KEY (id_produto) REFERENCES produtos(id),
            FOREIGN KEY (id_venda) REFERENCES vendas(id)
        )
        """
        self.cursor.execute(items_query)

        self.conn.commit()
