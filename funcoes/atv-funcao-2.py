import os
os.system('cls')

def positivo_negativo(numero):
    if numero < 0:
        print("===== RESPOSTA =====")
        print("ESSE NÚMERO É NEGATIVO! ")
    elif numero == 0:
        print("ESSE NÚMERO É NULO!")
    else:
        print("===== RESPOSTA =====")
        print("ESSE NÚMERO É POSITIVO!")
numero = int(input("INFORME UM NÚMERO: "))
positivo_negativo(numero)