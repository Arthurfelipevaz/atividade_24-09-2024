import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import pandas as pd
from pandas.plotting import table
import sqlite3
import os
import webbrowser

def obter_dados_cidades():
    conexao = sqlite3.connect('jaime.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT codcidade, nomecid, uf FROM cidade")
    dados_cidades = cursor.fetchall()
    cursor.close()
    conexao.close()
    lista_dados = [{"ID": row[0], "Cidade": row[1], "UF": row[2]} for row in dados_cidades]
    return lista_dados

def obter_dados_clientes():
    conexao = sqlite3.connect('jaime.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT idcliente, nome, telefone, email, codcidade FROM cliente")
    dados_clientes = cursor.fetchall()
    cursor.close()
    conexao.close()
    lista_dados = [{"ID": row[0], "Nome": row[1], "Telefone": row[2], "Email": row[3], "Código Cidade": row[4]} for row in dados_clientes]
    return lista_dados

def obter_dados_usuarios():
    conexao = sqlite3.connect('jaime.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT idusuario, nome, telefone, email, usuario FROM usuario")
    dados_usuarios = cursor.fetchall()
    cursor.close()
    conexao.close()
    lista_dados = [{"ID": row[0], "Nome": row[1], "Telefone": row[2], "Email": row[3], "Usuário": row[4]} for row in dados_usuarios]
    return lista_dados

def exportar_cidades_para_pdf():
    pdf_file = "cidades.pdf"
    dados_cidades = obter_dados_cidades()
    
    if dados_cidades:
        df_cidades = pd.DataFrame(dados_cidades)
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.axis('off')
        tabela = table(ax, df_cidades, loc='center', cellLoc='center', colWidths=[0.2]*len(df_cidades.columns))
        tabela.auto_set_font_size(False)
        tabela.set_fontsize(10)
        tabela.scale(1.2, 1.2)
        plt.savefig(pdf_file, bbox_inches='tight')
        plt.close(fig)
    
    escolher_acao(pdf_file)

def exportar_clientes_para_pdf():
    pdf_file = "clientes.pdf"
    dados_clientes = obter_dados_clientes()
    
    if dados_clientes:
        df_clientes = pd.DataFrame(dados_clientes)
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.axis('off')
        tabela = table(ax, df_clientes, loc='center', cellLoc='center', colWidths=[0.2]*len(df_clientes.columns))
        tabela.auto_set_font_size(False)
        tabela.set_fontsize(10)
        tabela.scale(1.2, 1.2)
        plt.savefig(pdf_file, bbox_inches='tight')
        plt.close(fig)
    
    escolher_acao(pdf_file)

def exportar_usuarios_para_pdf():
    pdf_file = "usuarios.pdf"
    dados_usuarios = obter_dados_usuarios()
    
    if dados_usuarios:
        df_usuarios = pd.DataFrame(dados_usuarios)
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.axis('off')
        tabela = table(ax, df_usuarios, loc='center', cellLoc='center', colWidths=[0.2]*len(df_usuarios.columns))
        tabela.auto_set_font_size(False)
        tabela.set_fontsize(10)
        tabela.scale(1.2, 1.2)
        plt.savefig(pdf_file, bbox_inches='tight')
        plt.close(fig)
    
    escolher_acao(pdf_file)

def escolher_acao(pdf_file):
    # Exibe a pergunta em um messagebox
    resposta = messagebox.askyesno("Exportar PDF", "Deseja abrir o PDF após exportar?")
    
    if resposta:  # Se o usuário escolher "Sim"
        abrir_pdf(pdf_file)
    else:
        messagebox.showinfo("PDF Exportado", f"O arquivo {pdf_file} foi exportado com sucesso.")

def abrir_pdf(pdf_file):
    # Abre o arquivo PDF no visualizador padrão do sistema
    if os.path.exists(pdf_file):
        webbrowser.open_new(pdf_file)
    else:
        messagebox.showerror("Erro", f"Arquivo {pdf_file} não encontrado.")

# Interface gráfica principal
root = tk.Tk()
root.title("Exportar Dados para PDF")

botao_exportar_cidades = tk.Button(root, text="Exportar Cidades", command=exportar_cidades_para_pdf)
botao_exportar_cidades.pack(pady=10)

botao_exportar_clientes = tk.Button(root, text="Exportar Clientes", command=exportar_clientes_para_pdf)
botao_exportar_clientes.pack(pady=10)

botao_exportar_usuarios = tk.Button(root, text="Exportar Usuários", command=exportar_usuarios_para_pdf)
botao_exportar_usuarios.pack(pady=10)

root.state("zoomed")
root.mainloop()
