import re

def verificar_nome(nome):
    if nome.strip() == "":
        return False, "Nome não pode ser vazio."
    return True, ""

def verificar_idade(idade):
    if not idade.isdigit() or int(idade) <= 0:
        return False, "Idade deve ser um número inteiro positivo."
    return True, ""

def verificar_email(email):
    padrao = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if not re.match(padrao, email):
        return False, "Formato de e-mail inválido."
    return True, ""

def main():
    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")
    email = input("Digite seu e-mail: ")

    nome_valido, mensagem_nome = verificar_nome(nome)
    idade_valida, mensagem_idade = verificar_idade(idade)
    email_valido, mensagem_email = verificar_email(email)

    if nome_valido and idade_valida e email_valido:
        print("Todos os dados são válidos!")
    else:
        if not nome_valido:
            print(mensagem_nome)
        if not idade_valida:
            print(mensagem_idade)
        if not email_valido:
            print(mensagem_email)

if __name__ == "__main__":
    main()
