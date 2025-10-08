import os
import time

os.system('cls')

# Função sem parâmetros e sem retorno.
def limpa_tela():
    time.sleep(2) # Espera 3 segundos.
    os.system("cls")

def converter(n1):
    return n1 * 100

def resultado(posicao1):
    print("\n")
    print("====== RESPOSTA ======")
    print(f"valor em centímetros: {posicao1:.2f}")

limpa_tela()

metros = float(input("INFORME UM VALOR EM METROS: "))

posicao1 = converter(metros)
resultado(posicao1)