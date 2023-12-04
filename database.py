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

def adicionar_produto(conn, produto):
    cursor = None
    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO produtos (nome, preco, quantidade) VALUES (%s, %s, %s)
        ''', produto.obter_dados())
        conn.commit()

        id_produto = cursor.lastrowid
        print(f"\nProduto cadastrado com sucesso! ID do produto: {id_produto}")
        return id_produto
    
    except mysql.connector.Error as err:
        print(f"Erro: {err}")
    finally:
        if cursor:
            cursor.close()
        if conn.is_connected():
            conn.close()

def adicionar_cliente(conn, cliente):
    cursor = None
    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO clientes (nome, telefone, endereco) VALUES (%s, %s, %s)
        ''', cliente.obter_dados())
        conn.commit()

        id_cliente = cursor.lastrowid
        print(f"\nCliente cadastrado com sucesso! ID do cliente: {id_cliente}")
        return id_cliente
    except mysql.connector.Error as err:
        print(f"Erro: {err}")
    finally:
        if cursor:
            cursor.close()
        if conn.is_connected():
            conn.close()

def adicionar_venda(conn, venda):
    cursor = None
    try:
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO vendas (data, total, cliente_id) VALUES (%s, %s, %s)
        ''', venda.obter_dados())

        conn.commit()
        return cursor.lastrowid

    except mysql.connector.Error as err:
        print(f"Erro ao adicionar venda: {err}")
        return None

    finally:
        if cursor:
            cursor.close()
        if conn.is_connected():
            conn.close()

def atualizar_estoque(conn, produto_id, quantidade):
    cursor = None
    try:
        cursor = conn.cursor()

        cursor.execute('''
            UPDATE produtos SET quantidade = quantidade - %s WHERE id = %s
        ''', (quantidade, produto_id))

        conn.commit()

    except mysql.connector.Error as err:
        print(f"Erro ao atualizar estoque: {err}")

    finally:
        if cursor:
            cursor.close()
        if conn.is_connected():
            conn.close()

def adicionar_item_venda(conn, venda_id, produto_id, quantidade, subtotal):
    cursor = None
    try:
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO itens_venda (id_venda, id_produto, quantidade, subtotal) VALUES (%s, %s, %s, %s)
        ''', (venda_id, produto_id, quantidade, subtotal))

        conn.commit()

    except mysql.connector.Error as err:
        print(f"Erro ao adicionar item à venda: {err}")

    finally:
        if cursor:
            cursor.close()
        if conn.is_connected():
            conn.close()

def cliente_existe(conn, cliente_id):
    cursor = None
    try:
        cursor = conn.cursor()

        cursor.execute('''
            SELECT * FROM clientes WHERE id = %s
        ''', (cliente_id,))

        return cursor.fetchone() is not None

    except mysql.connector.Error as err:
        print(f"Erro ao verificar existência do cliente: {err}")
        return False

    finally:
        if cursor:
            cursor.close()
        if conn.is_connected():
            conn.close()

def produto_existe(conn, produto_id):
    cursor = None
    try:
        cursor = conn.cursor()

        cursor.execute('''
            SELECT * FROM produtos WHERE id = %s
        ''', (produto_id,))

        return cursor.fetchone() is not None

    except mysql.connector.Error as err:
        print(f"Erro ao verificar existência do produto: {err}")
        return False

    finally:
        if cursor:
            cursor.close()
        if conn.is_connected():
            conn.close()

def obter_preco_produto(conn, produto_id):
    cursor = None
    try:
        cursor = conn.cursor()

        cursor.execute('''
            SELECT preco FROM produtos WHERE id = %s
        ''', (produto_id,))

        return cursor.fetchone()[0]

    except mysql.connector.Error as err:
        print(f"Erro ao obter preço do produto: {err}")
        return None

    finally:
        if cursor:
            cursor.close()
        if conn.is_connected():
            conn.close()

def consultar_estoque(conn):
    cursor = None
    try:
        cursor = conn.cursor()

        cursor.execute('''
            SELECT id, nome, quantidade, preco FROM produtos
        ''')

        estoque = cursor.fetchall()

        print("\nEstoque:")
        for produto in estoque:
            print(f"ID: {produto[0]}, Nome: {produto[1]}, Quantidade: {produto[2]}, Preço: {produto[3]}")

    except mysql.connector.Error as err:
        print(f"Erro ao consultar estoque: {err}")

    finally:
        if cursor:
            cursor.close()
        if conn.is_connected():
            conn.close()

def gerar_relatorio(conn):
    cursor = None
    try:
        cursor = conn.cursor()

        cursor.execute('''
            SELECT v.id, v.data, c.nome AS cliente, SUM(iv.quantidade * p.preco) AS total
            FROM vendas v
            JOIN clientes c ON v.cliente_id = c.id
            JOIN itens_venda iv ON v.id = iv.id_venda
            JOIN produtos p ON iv.id_produto = p.id
            GROUP BY v.id, v.data, c.nome
        ''')

        relatorio = cursor.fetchall()

        print("\nRelatório de Vendas:")
        for venda in relatorio:
            print(f"ID: {venda[0]}, Data: {venda[1]}, Cliente: {venda[2]}, Total: R${venda[3]:.2f}")

    except mysql.connector.Error as err:
        print(f"Erro ao gerar relatório: {err}")

    finally:
        if cursor:
            cursor.close()
        if conn.is_connected():
            conn.close()