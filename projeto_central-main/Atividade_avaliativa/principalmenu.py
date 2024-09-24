import tkinter as tk
from tkinter import Menu

class MenuInicial:
    def __init__(self, root):
        self.root = root
        self.root.title("Menu Inicial")

        # Container principal
        self.container1 = tk.Frame(root)
        self.container1.pack()

    def abrir_usuario(self):
        from usuario import Usuario
        # Cria uma nova janela e instancia a classe Usuario
        nova_janela = tk.Toplevel(self.root)
        app = Usuario(nova_janela)

    def abrir_cidade(self):
        from cidade import Cidade
        # Cria uma nova janela e instancia a classe Cidade
        nova_janela = tk.Toplevel(self.root)
        app = Cidade(nova_janela)

    def abrir_clientes(self):
        from clientes import Clientes
        # Cria uma nova janela e instancia a classe Clientes
        nova_janela = tk.Toplevel(self.root)
        app = Clientes(nova_janela)

    def abrir_relatorio(self):
        from relatorio import Relatorio
        # Cria uma nova janela e instancia a classe Relatorio
        nova_janela = tk.Toplevel(self.root)
        app = Relatorio(nova_janela)

# Inicializa a aplicação
root = tk.Tk()

# Criação da instância da interface principal
app = MenuInicial(root)

# Criação da barra de menu
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)

# Adiciona comandos ao menu
filemenu.add_command(label="Cidade", command=app.abrir_cidade)
filemenu.add_command(label="Clientes", command=app.abrir_clientes)
filemenu.add_command(label="Usuario", command=app.abrir_usuario)
filemenu.add_command(label="Relatório", command=app.abrir_relatorio)  # Novo comando para Relatório
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

# Adiciona o menu "File" na barra de menus
menubar.add_cascade(label="File", menu=filemenu)

# Configura a janela principal para usar a barra de menu
root.config(menu=menubar)

# Configura a janela principal para abrir maximizada
root.state("zoomed")
root.mainloop()
