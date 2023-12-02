import database as db
from produto import Produto
from cliente import Cliente
from venda import Venda
from datetime import datetime

def main():
    db.criar_banco_dados()
    conn = db.conectar_banco_dados()

    if conn:
        db.criar_tabelas(conn)

        while True:
            print("\n1. Adicionar Cliente\n2. Adicionar Produto\n3. Realizar Venda\n4. Consultar Estoque\n5. Gerar Relatório\n6. Sair")
            escolha = input("Escolha uma opção: ")

            if escolha == "1":
                nome = input("\nDigite o nome do cliente: ")
                telefone = input("Digite o telefone do cliente: ")
                endereco = input("Digite o endereço do cliente: ")

                novo_cliente = Cliente(nome=nome, telefone=telefone, endereco=endereco)
                db.adicionar_cliente(conn, novo_cliente)
            
            elif escolha == "2":
                nome = input("\nNome do produto: ")
                preco = float(input("Preço do produto: "))
                quantidade = int(input("Quantidade: "))
                
                novo_produto = Produto(nome=nome, preco=preco, quantidade=quantidade)
                db.adicionar_produto(conn, novo_produto)


            elif escolha == "3":
                cliente_id = int(input("\nID do cliente: "))
                produto_id = int(input("ID do produto a ser vendido: "))
                quantidade = int(input("Quantidade a ser vendida: "))

                if db.cliente_existe(conn, cliente_id) and db.produto_existe(conn, produto_id):
                    preco_produto = db.obter_preco_produto(conn, produto_id)
                    total = quantidade * preco_produto

                    venda = Venda(data=datetime.now(), total=total, cliente_id=cliente_id)
                    venda_id = db.adicionar_venda(conn, venda)

                    db.atualizar_estoque(conn, produto_id, quantidade)
                    db.adicionar_item_venda(conn, venda_id, produto_id, quantidade, total)

                    print(f"\nVenda realizada com sucesso! ID da venda: {venda_id}")
                else:
                    print("\nCliente ou produto não encontrado. Verifique os IDs e tente novamente.")

            elif escolha == "4":
                db.consultar_estoque(conn)

            elif escolha == "5":
                db.gerar_relatorio(conn)

            elif escolha == "6":
                break

            else:
                print("\nOpção inválida. Tente novamente.")

        conn.close()

if __name__ == "__main__":
    main()