import os
os.system("cls")

# c_numeros_impare = []
# c_numeros_pares = []
# contador = 0
# numeros = 0

pares = 0
impares = 0
soma_pares = 0
soma_geral = 0
contador_geral = 0


while True:
    numero = int(input("DIGITE UM NÚMERO: "))
    if numero > 0:
        contador_geral = 1
        soma_geral += numero
        if numero % 2 == 0:
            pares += 1
            soma_pares += numero
        else:
            impares += 1
    if numero == 0:
        break

# media_pares = soma_pares / pares if pares != 0 else 0

if pares != 0:
    media_pares = soma_pares / pares
else:
    media_pares = 0

if contador_geral != 0:
    media_geral = soma_geral /contador_geral
else:
    media_geral = 0

print("\n========= RESULTADO =========")
print(f"QUANTIDADE DE PARES: {pares}")
print(f"QAUNTIDADE DED IMPAREES: {impares}")
print(f"MÉDIA DE NÚMEROS PARES: {media_pares}")
print(f"MÉDIA GERAL: {media_geral}")













# while True:
#     print("====== CONTADOR DE NÚMEROS ======")
#     numeros = int(input(f"INFORME O {contador + 1} NÚMERO: "))
    

#     if numeros < 0 :
#         break

#     contador += 1


#     if numeros % 2 == 0:
#         c_numeros_pares.append(numeros)
#     else:
#         c_numeros_impare.append(numeros)

#     media_geral = sum(c_numeros_impare + c_numeros_pares) / contador
#     media_pares = sum(c_numeros_pares) / contador 
        
# print("====== RESULTADOS =====")
# print(f"QUANTIDAE DE NÚMEROS PARES: {len(c_numeros_pares)}")
# print(f"MÉDIA: {media_pares}")
# print(F"MÉDIA GERAL: {media_geral}")



