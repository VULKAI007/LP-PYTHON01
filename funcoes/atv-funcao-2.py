# ATIVIDADE 2
# FAÇA UMA FUNÇÃO QUE RECEBE UM VALOR INTEIRO E VERIFICA SE O VALOR É POSITIVO OU NEGATIVO



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