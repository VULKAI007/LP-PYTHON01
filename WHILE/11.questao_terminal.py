import os
os.system("cls")


tentativas = 0
email = input("CADASTRE UM EMAIL: ")
c_senha = input("CADASTRE UMA SENHA:  ")


for i in range(3):
    while True:
        if tentativas <= 3:
            break
        print(f"TENTATIVAS: {tentativas }")
        login = input("DIGITE SEU LOGIN: ")
        senha= input("DIGITE SUA SENHA: ")

        if email == login and c_senha == senha:
            print("PARABÉM, LOGIN EFETUADO COM SUCEESSO!")
            break                               
        else:
            print("LOGIN OU SENHA INVÁLIDOS TENTE NOVAMENTE")
            tentativas += 1
            print("\n")
            