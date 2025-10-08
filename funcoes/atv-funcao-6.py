import os
import time

os.system('cls')

# Função sem parâmetros e sem retorno.
def limpa_tela():
    time.sleep(3) # Espera 3 segundos.
    os.system("cls")

# FUNÇÃO COM PARÊMETRO, RESPONSÁVEL POR SOMAR
def soma(n1, n2):
    cal_soma = n1 + n2
    return cal_soma

# FUNÇÃO COM PARÊMETRO, RESPONSÁVEL POR SUBTRAIR
def subtracao(n1, n2):
    cal_subtracao = n1 - n2
    return cal_subtracao

# FUNÇÃO COM PARÊMETRO, RESPONSÁVEL POR MULTIPLICAÇÃO
def multiplicacao(n1, n2):
    cal_multiplicao = n1 * n2
    return cal_multiplicao

# FUNÇÃO COM PARÊMETRO, RESPONSÁVEL POR DIVISÃO
def divisao(n1, n2):
    return n1 / n2 if n2 != 0 else "DIVISÃO POR ZERO"
    

# FUNÇÃO COM PARÂMETRO RESPONSÁVEL POR APRESENTAR OS RESULTADOS
def resultado(soma1, subtracao1, multiplicacao1, divisao1):
    print("\n")
    print("======== RESULTADO ========")
    print(f"SOMA: {soma1}")
    print(f"SUBTRAÇÃO: {subtracao1}")
    print(f"MULTIPLICAÇÃO: {multiplicacao1}")
    print(f"DIVISÃO: {divisao1}")

limpa_tela()

# VARIÁVEIS QUE VÃO ARMAZENAR AS INFORMÇÕES INSERIDAS PELO USUÁRIO
primeiro_numero = int(input("Digite um número: "))
segundo_numero = int(input("Digite um número: "))

# CHAMANDO AS FUNÇÕES E ASSOCIANDO AS VARIÁVEOS
soma1 = soma(primeiro_numero,segundo_numero)
subtracao1 = subtracao(primeiro_numero,segundo_numero)
multiplicacao1 = multiplicacao(primeiro_numero,segundo_numero)
divisao1 = divisao(primeiro_numero,segundo_numero)

resultado(soma1, subtracao1, multiplicacao1, divisao1)