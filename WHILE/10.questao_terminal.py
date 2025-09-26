import os
os.system("cls")

email = input("CADASTRE UM EMAIL: ")
c_senha = input("CADASTRE UMA SENHA:  ")



while True:
    login = input("DIGITE SEU LOGIN: ")
    senha= input("DIGITE SUA SENHA: ")

    if email == login and c_senha == senha:
        print("PARABÉM, LOGIN EFETUADO COM SUCEESSO!")
        break
    else:
        print("LOGIN OU SENHA INVÁLIDOS TENTE NOVAMENTE")
        print("\n")