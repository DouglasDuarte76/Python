pip install bandit semgrep

_____________________________________

import os
import sqlite3

def buscar_usuario(nome):
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM usuarios WHERE nome = '{nome}'"  # Vulnerável a SQL Injection!
    cursor.execute(query)
    return cursor.fetchall()

def executar_comando_usuario(comando):
    os.system(comando)  # PERIGO! Pode executar qualquer comando do sistema.

def ler_arquivo(nome_arquivo):
    with open(nome_arquivo, "r") as file:
        return file.read()  # Pode permitir leitura de arquivos sensíveis.

def conectar_servidor():
    senha = "123456"  # Credencial hardcoded! Nunca faça isso.
    print(f"Conectando com a senha: {senha}")

nome = input("Digite seu nome: ")
print(buscar_usuario(nome))

comando = input("Digite um comando: ")
executar_comando_usuario(comando)

_____________________________________

bandit -r codigo_inseguro.py

_____________________________________

semgrep --config auto codigo_inseguro.py

_____________________________________

import os
import sqlite3

def buscar_usuario(nome):
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    query = "SELECT * FROM usuarios WHERE nome = ?"  # USO SEGURO DE PARAMETRIZAÇÃO
    cursor.execute(query, (nome,))
    return cursor.fetchall()

def executar_comando_usuario(comando):
    comandos_permitidos = ["ls", "whoami"]
    if comando in comandos_permitidos:
        os.system(comando)  # Execução controlada
    else:
        print("Comando não permitido!")

def ler_arquivo(nome_arquivo):
    arquivos_permitidos = ["log.txt", "config.json"]
    if nome_arquivo in arquivos_permitidos:
        with open(nome_arquivo, "r") as file:
            return file.read()
    else:
        print("Acesso negado ao arquivo!")

def conectar_servidor():
    from getpass import getpass
    senha = getpass("Digite a senha: ")  # Pedir a senha ao invés de armazená-la no código.
    print("Conectado com segurança!")

nome = input("Digite seu nome: ")
print(buscar_usuario(nome))

comando = input("Digite um comando permitido: ")
executar_comando_usuario(comando)



