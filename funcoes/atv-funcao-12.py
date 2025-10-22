# escreva um program que solicite ao utilizador o fornecimento deo seu peso em KG e de sua altura em M
# e a partir deles calcule o indicé de massa corpórea do utilizador.

import os
os.system('cls')

def calcular_imc(peso,altura):
    return peso / (altura **2)

def resultado(imc):
    print("===== RESULTADO =====")
    print(f"IMC: {imc:.2f}")

peso = float(input("INFORME SEU PESO(kg): "))
altura = float(input("INFORME SUA ALTURA(m): "))

imc = calcular_imc(peso,altura)
resultado(imc)