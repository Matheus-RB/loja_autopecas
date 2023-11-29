import database as db
from produto import Produto
from cliente import Cliente
from venda import Venda


def main():
    db.criar_banco_dados()
    conn = db.conectar_banco_dados()

    if conn:
        db.criar_tabelas(conn)

        while True:
            print("\n1. Adicionar Produto\n2. Adicionar Cliente\n3. Realizar Venda\n4. Gerar Relatorio\n5. Sair")
            escolha = input("Escolha uma opção: ")

            if escolha == "1":
                nome = input("\nNome do produto: ")
                preco = float(input("Preço do produto: "))
                quantidade = int(input("Quantidade em estoque: "))
                
                # Criar uma instância de Produto
                produto = Produto()
                produto.adicionar_produto(conn, nome, preco, quantidade)

            elif escolha == "2":
                nome = input("Digite o nome do cliente: ")
                telefone = input("Digite o telefone do cliente: ")
                endereco = input("Digite o endereço do cliente: ")

                # Criar um novo cliente com os dados fornecidos
                novo_cliente = Cliente(nome=nome, telefone=telefone, endereco=endereco)

                # Adicionar o cliente ao banco de dados
                db.adicionarCliente(novo_cliente)

            elif escolha == "3":
                produtos = []
                while True:
                    produto_id = int(input("\nID do produto (0 para encerrar): "))
                    if produto_id == 0:
                        break
                    quantidade = int(input("Quantidade: "))
                    produtos.append((produto_id, quantidade))

                cliente_id = int(input("ID do cliente: "))
                
                # Criar uma instância de Venda
                venda = Venda(conn, cliente_id)
                
                # Adicionar itens à venda
                for produto_id, quantidade in produtos:
                    venda.adicionar_item(produto_id, quantidade)
                
                # Finalizar a venda
                venda.finalizar_venda()

            elif escolha == "4":
                venda_id = int(input("ID da venda: "))
                venda = Venda(conn, cliente_id)
                venda.id = venda_id
                venda.gerar_relatorio()

            elif escolha == "5":
                break

            else:
                print("Opção inválida. Tente novamente.")

        conn.close()

if __name__ == "__main__":
    main()