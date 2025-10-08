
# ATIVIDADE 4
# FAÇA UM PROGRAMA QUE IMPRIME A TABUADA DE UM NÚMERO INFORMADO PELO USUÁRIO DE 1 A 10
# UTILIZANDO UMA FUNÇÃO PARA EXIBIR O RESULTADO


import os
os.system('cls')
n = 0

def tabuado(numero):
    print("===== TABUADA =====")
    for i in range(1,11):
        n = numero + i
        print(f" {numero} X {i} = {n}")
numero = int(input("INFORME UM NÚMERO PARA ADQUIRIR A TABUADA: "))
tabuado(numero)