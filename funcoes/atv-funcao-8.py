import os
import time

os.system('cls')

# Função sem parâmetros e sem retorno.
def limpa_tela():
    time.sleep(2) # Espera 3 segundos.
    os.system("cls")

def inflacao(n1):
    if n1 < 100:
        return n1 + n1 * 0.10
    else:
        return n1 + n1 * 0.20

def resultado(posicao1):
    print("===== RESULTADO =====")
    print(f"PREÇO APÓS INFLAÇÃO: {posicao1:.2f}")

valor_solicitado = float(input("INFORME O VALOR PARA SER CORRIJIDO: "))
limpa_tela()
posicao1 = inflacao(valor_solicitado)
resultado(posicao1)