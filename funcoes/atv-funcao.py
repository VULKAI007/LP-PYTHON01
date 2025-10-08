# ATIVIDADE 1
# CRIE UMA FUNÇÃO QUE RECEBA UM NÚMERO E MOSTRE UMA MENSAGEM INFORMANDO
# SE O NÚMERO É ÁAR UM ÍMPAR


import os
os.system('cls')

def par_impar(numero):
    if numero % 2 == 0:
        print("O NÚMERO INFORMADO É PAR!")
    else:
        print("O NÚMERO INFORMADO É ÍMPAR!")
numero = int(input("DIGITE UM NÚMERO: "))
par_impar(numero)
    