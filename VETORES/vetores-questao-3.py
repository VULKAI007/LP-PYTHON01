# CRIE UM PROGRAMA QUE LEIA 6B NÚMEROS, ARMAZENANDO EM UM VETOR E INFORME QUANTOS SÃO PARES E QUANTOS SÃO ÍMPARES.
# MOSTRE OS NÚMEROS INFORMADOS PELO USUÁRIO.

import os
os.system('cls')

lista_numeros = []
pares = 0
impares = 0
QUANTIDADE = 6

for i in range(QUANTIDADE):
    numero = int(input(f"INFORMe O {i + 1}ª NÚMERO: "))
    lista_numeros.append(numero)

for i in lista_numeros:
    if i % 2 == 0:
        pares += 1
    else:
        impares += 1


print("====== RESULTADO =====")
for numero in lista_numeros:
    print(f"NÚMERO: {numero}")
print(f"QUANTIDADE DE NÚMEROS PARES: {pares}")
print(f"QUANTIDADE DE NÚMEROS ÍMPARES: {impares}")
















# lista_pares = []
# lista_impar = []


# for i in range(6):
#     numero = int(input(f"INFORM E O {i + 1} NÚMERO: "))
#     if numero % 2 == 0:
#         lista_pares.append(numero)
#     else:
#         lista_impar.append(numero)

# print("===== RESULTADO ======")
# print(f"LISTA DE NÚMEROS PARES: {lista_pares}")
# print(f"LISTA DE NÚMEROS ÍMPARES: {lista_impar}")
# print(f"QTD.NÚMEROS PARES: {len(lista_pares)}")
# print(f"QTD.NÚMEROS ÍMPARES: {len(lista_impar)}")