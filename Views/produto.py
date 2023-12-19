import tkinter as tk
from Controllers.produto_controller import ProdutoController

class ProdutoView:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro de Produto")

        self.controller = ProdutoController()

        tk.Label(root, text="Nome:").pack(pady=5)
        self.nome_entry = tk.Entry(root)
        self.nome_entry.pack(pady=5)

        tk.Label(root, text="Preço:").pack(pady=5)
        self.preco_entry = tk.Entry(root)
        self.preco_entry.pack(pady=5)

        tk.Label(root, text="Quantidade:").pack(pady=5)
        self.quantidade_entry = tk.Entry(root)
        self.quantidade_entry.pack(pady=5)

        add_button = tk.Button(root, text="Adicionar Produto", command=self.adicionar_produto)
        add_button.pack(pady=10)

        back_button = tk.Button(root, text="Voltar", command=self.voltar_tela_principal)
        back_button.pack(pady=10)

    def adicionar_produto(self):
        nome = self.nome_entry.get()
        preco = self.preco_entry.get()
        quantidade = self.quantidade_entry.get()

        self.controller.adicionar_produto(nome, preco, quantidade)
        print("Produto adicionado com sucesso!")

        self.root.destroy()

    def voltar_tela_principal(self):
        self.root.destroy()