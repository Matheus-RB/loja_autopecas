import tkinter as tk
from Views.cliente import ClienteView
from Views.produto import ProdutoView
from Views.venda import VendaView
from Views.relatorio import RelatorioView
from Views.estoque import EstoqueView

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Cadastros")

        cliente_button = tk.Button(root, text="Cadastrar Cliente", command=self.cadastrar_cliente)
        cliente_button.pack(pady=10)
        
        produto_button = tk.Button(root, text="Cadastrar Produto", command=self.cadastrar_produto)
        produto_button.pack(pady=10)
        
        venda_button = tk.Button(root, text="Realizar Venda", command=self.realizar_venda)
        venda_button.pack(pady=10)
        
        estoque_button = tk.Button(root, text="Consultar Estoque", command=self.consultar_estoque)
        estoque_button.pack(pady=10)
        
        relatorio_button = tk.Button(root, text="Gerar Relatório", command=self.gerar_relatorio)
        relatorio_button.pack(pady=10)
        
        exit_button = tk.Button(root, text="Sair", command=root.quit)
        exit_button.pack(pady=10)

    def cadastrar_cliente(self):
        root = tk.Toplevel(self.root)
        cliente_view = ClienteView(root)
  
    def cadastrar_produto(self):
        root = tk.Toplevel(self.root)
        produto_view = ProdutoView(root)
        
    def realizar_venda(self):
        root = tk.Toplevel(self.root)
        venda_view = VendaView(root)

    def gerar_relatorio(self):
        root = tk.Toplevel(self.root)
        relatorio_view = RelatorioView(root)
        
    def consultar_estoque(self):
        root = tk.Toplevel(self.root)
        estoque_view = EstoqueView(root)

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
