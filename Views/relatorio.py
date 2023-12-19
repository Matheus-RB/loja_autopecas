import tkinter as tk
from Controllers.relatorio_controller import RelatorioController

class RelatorioView:
    def __init__(self, root):
        self.root = root
        self.root.title("Relatório de Vendas")

        self.controller = RelatorioController()

        relatorio_button = tk.Button(root, text="Gerar Relatório", command=self.exibir_relatorio)
        relatorio_button.pack(pady=10)

        self.text_area = tk.Text(root, height=20, width=50)
        self.text_area.pack(pady=10)

        back_button = tk.Button(root, text="Voltar", command=self.voltar_tela_principal)
        back_button.pack(pady=10)

    def exibir_relatorio(self):
        vendas = self.controller.obter_relatorio_vendas()

        self.text_area.delete(1.0, tk.END)

        for venda in vendas:
            venda_str = f"ID: {venda[0]}, Data: {venda[1]}, Total: R${venda[2]:.2f}, Cliente: {venda[3]}\n"
            self.text_area.insert(tk.END, venda_str)

    def voltar_tela_principal(self):
        self.root.destroy()
