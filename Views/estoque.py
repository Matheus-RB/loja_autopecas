import tkinter as tk
from Controllers.estoque_controller import EstoqueController

class EstoqueView:
    def __init__(self, root):
        self.root = root
        self.root.title("Consulta de Estoque")

        self.controller = EstoqueController()

        consultar_button = tk.Button(root, text="Consultar Estoque", command=self.consultar_estoque)
        consultar_button.pack(pady=10)

        self.text_area = tk.Text(root, height=20, width=50)
        self.text_area.pack(pady=10)

        back_button = tk.Button(root, text="Voltar", command=self.voltar_tela_principal)
        back_button.pack(pady=10)

    def consultar_estoque(self):
        estoque = self.controller.consultar_estoque()

        self.text_area.delete(1.0, tk.END)

        for produto in estoque:
            produto_str = f"ID: {produto[0]}, Nome: {produto[1]}, Quantidade: {produto[2]}\n"
            self.text_area.insert(tk.END, produto_str)

    def voltar_tela_principal(self):
        self.root.destroy()
