import tkinter as tk
from tkinter import messagebox

# Criar a janela principal
janela = tk.Tk()
janela.title("Calculadora Simples")

# Definir o tamanho da janela
janela.geometry("400x500")

# Entrada para os números e operações
entrada = tk.Entry(janela, width=16, font=("Arial", 24), borderwidth=2, relief="solid")
entrada.grid(row=0, column=0, columnspan=4)

# Função para adicionar texto na entrada
def adicionar_texto(texto):
    entrada.insert(tk.END, texto)

# Função para calcular o resultado
def calcular():
    try:
        resultado = eval(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(resultado))
    except Exception as e:
        messagebox.showerror("Erro", "Entrada inválida")

# Função para limpar a entrada
def limpar():
    entrada.delete(0, tk.END)

# Botões da calculadora
botoes = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("+", 4, 2), ("=", 4, 3),
    ("C", 5, 0)
]

for (texto, linha, coluna) in botoes:
    if texto == "=":
        btn = tk.Button(janela, text=texto, width=10, height=3, command=calcular)
    elif texto == "C":
        btn = tk.Button(janela, text=texto, width=10, height=3, command=limpar)
    else:
        btn = tk.Button(janela, text=texto, width=10, height=3, command=lambda t=texto: adicionar_texto(t))
    btn.grid(row=linha, column=coluna)

# Executar o loop principal
janela.mainloop()
