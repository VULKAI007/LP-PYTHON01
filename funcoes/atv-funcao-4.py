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