2.2022 CENTRO QP INTROD À PROGRAMAÇÃO EM PYTHON B - TARDE
LINGUAGEM DE PROGRAMAÇÃO PYTHON - JOSE AUGUSTO POLIZELLO
Criando janelas com Tkinter.
# para consulta: https://realpython.com/python-gui-tkinter/
'''

# aula 1 - criando uma janela
from tkinter import Tk

janela = Tk()
# gera um loop constante para a janela permanecer na tela
janela.mainloop()
#___________________


# aula 2 - gerando um mensagem numa janela
# importamos todo o módulo
import tkinter as tk

# instanciamos a classe TK do módulo tk
janela = tk.Tk()

janela.title("Cotação de Moedas")
# cria o label
mensagem = tk.Label(text="Sistema de Busca de Cotação de Moedas")
# coloca o label na caixa
mensagem.pack()

mensagem2 = tk.Label(text="Selecione a moeda desejada")
mensagem2.pack()

janela.mainloop()
#___________________


# aula 3 - cores das janelas
import tkinter as tk

janela = tk.Tk()

janela.title("Cotação de Moedas")

mensagem = tk.Label(text="Sistema de Busca de Cotação de Moedas", fg='white', bg='black', width=50, height=10)
mensagem.pack()

mensagem2 = tk.Label(text="Selecione a moeda desejada", height=15, width=70)
mensagem2.pack()

janela.mainloop()
#___________________


# aula 4 - caixa de entrada (tk.Entry())
import tkinter as tk

janela = tk.Tk()

janela.title("Cotação de Moedas")

mensagem = tk.Label(text="Sistema de Busca de Cotação de Moedas", fg='white', bg='black', width=35, height=5)
mensagem.pack()

mensagem2 = tk.Label(text="Selecione a moeda desejada")
mensagem2.pack()

# cria a caixa de entrada
moeda = tk.Entry()
moeda.pack()

janela.mainloop()
#___________________


# aula 5 - ajustes dos objetos
# https://www.tutorialspoint.com/python/tk_grid.htm

import tkinter as tk

janela = tk.Tk()

janela.title("Cotação de Moedas")

# redimencionamento automático dos objetos
# padrão weight=0 não ajusta automaticamente
janela.rowconfigure(0, weight=1)
# columnconfigure[0,1] para ajustar as duas colunas
janela.columnconfigure([0, 1], weight=1)

# troca do pack pelo grid
# columnspan ocupa quantas colunas eu quiser
# stick ajusta o objeto nas direções que quiser NSEW
mensagem = tk.Label(text="Sistema de Busca de Cotação de Moedas", fg='white', bg='black', width=35, height=5)
mensagem.grid(row=0, column=0, columnspan=2, sticky="NSEW")

mensagem2 = tk.Label(text="Selecione a moeda desejada")
mensagem2.grid(row=1, column=0)

moeda = tk.Entry()
moeda.grid(row=1, column=1)

janela.mainloop()
#___________________


# aula 6 - inserindo botões para interagir com a janela
import tkinter as tk

janela = tk.Tk()

janela.title("Cotação de Moedas")

janela.rowconfigure(0, weight=1)
janela.columnconfigure([0, 1], weight=1)

mensagem = tk.Label(text="Sistema de Busca de Cotação de Moedas", fg='white', bg='black', width=35, height=5)
mensagem.grid(row=0, column=0, columnspan=2, sticky="NSEW")

mensagem2 = tk.Label(text="Selecione a moeda desejada")
mensagem2.grid(row=1, column=0)

moeda = tk.Entry()
moeda.grid(row=1, column=1)


# função para o comando do botão
def buscar_cotacao():
    print(moeda.get())


# cria botão na janela
botao = tk.Button(text="Buscar Cotação", command=buscar_cotacao)
botao.grid(row=2, column=1)

janela.mainloop()
#___________________


# aula 7 - retornando a resposta da cotação para o usuário
import tkinter as tk

janela = tk.Tk()

janela.title("Cotação de Moedas")

janela.rowconfigure(0, weight=1)
janela.columnconfigure([0, 1], weight=1)

mensagem = tk.Label(text="Sistema de Busca de Cotação de Moedas", fg='white', bg='black', width=35, height=5)
mensagem.grid(row=0, column=0, columnspan=2, sticky="NSEW")

mensagem2 = tk.Label(text="Selecione a moeda desejada")
mensagem2.grid(row=1, column=0)

moeda = tk.Entry()
moeda.grid(row=1, column=1)


dicionario_cotacoes = {
    'Dólar': 5.47,
    'Euro': 6.68,
    'Bitcoin': 20000,
}


def buscar_cotacao():
    moeda_preenchida = moeda.get()
    cotacao_moeda = dicionario_cotacoes.get(moeda_preenchida)
    mensagem_cotacao = tk.Label(text="        Cotação não encontrada      ")
    # mensagem impressa na linha 4, coluna 1
    mensagem_cotacao.grid(row=3, column=0)
    if cotacao_moeda:
        # muda o parâmetro "text" para outro texto
        mensagem_cotacao["text"] = f'Cotação do {moeda_preenchida} é de {cotacao_moeda} reais'


botao = tk.Button(text="Buscar Cotação", command=buscar_cotacao)
botao.grid(row=2, column=1)

janela.mainloop()
#___________________
'''

# aula 8 - lista suspensa
import tkinter as tk
# importa a classe ttk
from tkinter import ttk

janela = tk.Tk()

janela.title("Cotação de Moedas")

janela.rowconfigure(0, weight=1)
janela.columnconfigure([0, 1], weight=1)

mensagem = tk.Label(text="Sistema de Busca de Cotação de Moedas", fg='white', bg='black', width=35, height=5)
mensagem.grid(row=0, column=0, columnspan=2, sticky="NSEW")

mensagem2 = tk.Label(text="Selecione a moeda desejada")
mensagem2.grid(row=1, column=0)

# tira a caixa de entrada para colocar a lista suspensa
# moeda = tk.Entry()
# moeda.grid(row=1, column=1)


dicionario_cotacoes = {
    'Dólar': 5.47,
    'Euro': 6.68,
    'Bitcoin': 20000,
}

# transforma o dicionário em uma lista
moedas = list(dicionario_cotacoes.keys())

# para a lista moedas para a combobox que vai ficar dentro da janela
moeda = ttk.Combobox(janela, values=moedas)
moeda.grid(row=1, column=1)


def buscar_cotacao():
    moeda_preenchida = moeda.get()
    cotacao_moeda = dicionario_cotacoes.get(moeda_preenchida)
    mensagem_cotacao = tk.Label(text="Cotação não encontrada")
    mensagem_cotacao.grid(row=3, column=0)
    if cotacao_moeda:
        mensagem_cotacao["text"] = f'Cotação do {moeda_preenchida} é de {cotacao_moeda} reais'


botao = tk.Button(text="Buscar Cotação", command=buscar_cotacao)
botao.grid(row=2, column=1)

janela.mainloop()
