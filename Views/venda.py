import tkinter as tk
from Controllers.venda_controller import VendaController

class VendaView:
    def __init__(self, root):
        self.root = root
        self.root.title("Realizar Venda")

        self.controller = VendaController()

        tk.Label(root, text="Cliente ID:").pack(pady=5)
        self.cliente_id_entry = tk.Entry(root)
        self.cliente_id_entry.pack(pady=5)

        tk.Label(root, text="Produto ID:").pack(pady=5)
        self.produto_id_entry = tk.Entry(root)
        self.produto_id_entry.pack(pady=5)

        tk.Label(root, text="Quantidade:").pack(pady=5)
        self.quantidade_entry = tk.Entry(root)
        self.quantidade_entry.pack(pady=5)

        add_button = tk.Button(root, text="Realizar Venda", command=self.realizar_venda)
        add_button.pack(pady=10)

        back_button = tk.Button(root, text="Voltar", command=self.voltar_tela_principal)
        back_button.pack(pady=10)

    def realizar_venda(self):
        cliente_id = self.cliente_id_entry.get()
        produto_id = self.produto_id_entry.get()
        quantidade = self.quantidade_entry.get()

        venda_id = self.controller.realizar_venda(cliente_id, produto_id, quantidade)
        print(f"Venda realizada com sucesso! ID: {venda_id}")

        self.root.destroy()

    def voltar_tela_principal(self):
        self.root.destroy()