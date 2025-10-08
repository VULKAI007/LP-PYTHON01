import os
import time
import datetime

os.system('cls')
ano_atual = datetime.date.today().year

# # Função sem parâmetros e sem retorno.
# def limpa_tela():
#     time.sleep(2) # Espera 3 segundos.
#     os.system("cls")

def conversor_idade(n1):
    return ano_atual - n1 if n1!= 0 else "INFORME UM ANO DE NASCIMENTO VÁLIDO!"

def resultado(posicao1):
    print("\n")
    print("===== RESULTADO =====")
    print(f"IDADE: {posicao1}")

ano_nascimento = int(input("INFORME SEU ANO DE NASCIMENTO: "))
posicao1 = conversor_idade(ano_nascimento)
resultado(posicao1)

