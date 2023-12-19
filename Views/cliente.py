import tkinter as tk
from Controllers.cliente_controller import ClienteController

class ClienteView:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro de Cliente")

        self.controller = ClienteController()

        tk.Label(root, text="Nome:").pack(pady=5)
        self.nome_entry = tk.Entry(root)
        self.nome_entry.pack(pady=5)

        tk.Label(root, text="Telefone:").pack(pady=5)
        self.telefone_entry = tk.Entry(root)
        self.telefone_entry.pack(pady=5)

        tk.Label(root, text="Endereço:").pack(pady=5)
        self.endereco_entry = tk.Entry(root)
        self.endereco_entry.pack(pady=5)

        add_button = tk.Button(root, text="Adicionar Cliente", command=self.adicionar_cliente)
        add_button.pack(pady=10)

        back_button = tk.Button(root, text="Voltar", command=self.voltar_tela_principal)
        back_button.pack(pady=10)

    def adicionar_cliente(self):
        nome = self.nome_entry.get()
        telefone = self.telefone_entry.get()
        endereco = self.endereco_entry.get()

        self.controller.adicionar_cliente(nome, telefone, endereco)
        print("Cliente adicionado com sucesso!")

        self.root.destroy()

    def voltar_tela_principal(self):
        self.root.destroy()
