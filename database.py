import mysql.connector

def criar_banco_dados():
    try:
        connection = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
        )

        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS loja_autopecas")
    except mysql.connector.Error as err:
        print(f"Erro: {err}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals():
            connection.close()

def conectar_banco_dados():
    try:
        conn = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            database="loja_autopecas"
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Erro: {err}")
        return None

def criar_tabelas(conn):
    try:
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS produtos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(255),
                preco FLOAT,
                quantidade INT
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS clientes (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(255),
                telefone VARCHAR(15),
                endereco VARCHAR(255)
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS vendas (
                id INT AUTO_INCREMENT PRIMARY KEY,
                data DATETIME,
                total FLOAT,
                cliente_id INT,
                FOREIGN KEY (cliente_id) REFERENCES clientes(id)
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS itens_venda (
                id INT AUTO_INCREMENT PRIMARY KEY,
                id_produto INT,
                id_venda INT,
                quantidade INT,
                subtotal FLOAT,
                FOREIGN KEY (id_produto) REFERENCES produtos(id),
                FOREIGN KEY (id_venda) REFERENCES vendas(id)
            )
        ''')
    except mysql.connector.Error as err:
        print(f"Erro: {err}")
    finally:
        if 'cursor' in locals():
            cursor.close()


def adicionarCliente(cliente):
    try:
        connection = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            database="loja_autopecas"
        )

        cursor = connection.cursor()
        cursor.execute('''
            INSERT INTO clientes (nome, telefone, endereco) VALUES (%s, %s, %s)
        ''', cliente.obter_dados_para_banco())
        connection.commit()
    except mysql.connector.Error as err:
        print(f"Erro: {err}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals():
            connection.close()
