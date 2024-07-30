import tkinter as tk
import sqlite3
import pandas as pd

#conexao = sqlite3.connect('produtos.db')

# Criando o cursor:
#c = conexao.cursor()

# Criando a tabela:
#c.execute("""CREATE TABLE produtos (
   #nome do produto text,
   #quantidade do produto text,
   #valor do produto text
#)""")

 #Commit as mudanças:
#conexao.commit()

 #Fechar o banco de dados:
#conexao.close()

#Criando Janela:
janela = tk.Tk()
janela.title('Cadastro de Produtos')
janela.geometry("330x250")


def cadastrar_produtos():
    conexao = sqlite3.connect('produtos.db')
    c = conexao.cursor()

    #Inserir dados na tabela:
    c.execute("INSERT INTO produtos VALUES (:produto,:quantidade,:valor)",
              {
                  'produto': entry_produto.get(),
                  'quantidade': entry_quantidade.get(),
                  'valor': entry_valor.get()
              })


    # Commit as mudanças:
    conexao.commit()

    # Fechar o banco de dados:
    conexao.close()

    # #Apaga os valores das caixas de entrada
    entry_produto.delete(0,"end")
    entry_quantidade.delete(0,"end")
    entry_valor.delete(0,"end")

def exportar_produtos():
    conexao = sqlite3.connect('produtos.db')
    c = conexao.cursor()

    # Selecionar dados da tabela:
    c.execute("SELECT *, oid FROM produtos")
    produtos_cadastrados = c.fetchall()
    
    # Transformar em DataFrame
    produtos_cadastrados = pd.DataFrame(produtos_cadastrados, columns=['produto', 'quantidade', 'valor', 'Id_banco'])
    
    # Exportar para Excel
    produtos_cadastrados.to_excel('produtos.xlsx')

    # Commit as mudanças:
    conexao.commit()

    # Fechar o banco de dados:
    conexao.close()


#Rótulos Entradas:
label_produto = tk.Label(janela, text='Produto')
label_produto.grid(row=0,column=0, padx=10, pady=10)

label_quantidade = tk.Label(janela, text='Quantidade')
label_quantidade.grid(row=1, column=0, padx=10, pady=10)

label_valor = tk.Label(janela, text='Valor')
label_valor.grid(row=2, column=0 , padx=10, pady=10)

#Caixas Entradas:
entry_produto = tk.Entry(janela , width =35)
entry_produto.grid(row=0,column=1, padx=10, pady=10)

entry_quantidade = tk.Entry(janela, width =35)
entry_quantidade.grid(row=1, column=1, padx=10, pady=10)

entry_valor = tk.Entry(janela, width =35)
entry_valor.grid(row=2, column=1 , padx=10, pady=10)

# Botão de Cadastrar

botao_cadastrar = tk.Button(text='Cadastrar Produto', command=cadastrar_produtos)
botao_cadastrar.grid(row=4, column=0,columnspan=2, padx=10, pady=10 , ipadx = 80)

# Botão de Exportar

botao_exportar = tk.Button(text='Exportar para Excel', command=exportar_produtos)
botao_exportar.grid(row=5, column=0,columnspan=2, padx=10, pady=10 , ipadx = 80)


janela.mainloop()