import os
os.system('cls')

print("----- CADASTRO USUÁRIO ------")
c_email = input("DIGITE SEU EMAIL: ").lower()
c_senha = input("DIGITE SUA SENHA: ")

print("------------------------------")
print("CADASTRO EFETUADO COM SUCESSO!")
print("\n")

print("----- LOGIN USUÁRIOS ------")
u_email = input("DIGITE SEU EMAIL CADASTRADO: ").lower()
u_senha = input("DIGITE SUA SENHA CADASTRADO: ")

if u_email == c_email and u_senha == c_senha:
    print("LOGIN EFETUADO COM SUCESSO!!")
else:
    print("LOGIN OU SENHA INVÁLIDOS")





"""""
email = "MELHOR"
senha = "1234"

email_u = input("DIGITE SEU EMAIL: ")
senha_u = str(input("DIGITE SUA SENHA: "))
email_u = email_u.upper()

if email_u == email and senha_u == senha:
    print("BEM VINDO, USUÁRIO!")
else:
    print("LOGIN OU SENHA INVÁLIDOS!!")
"""
