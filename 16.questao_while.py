import os
os.system("cls")

c_numeros_impare = []
c_numeros_pares = []
contador = 0
numeros = 0


while True:
    print("====== CONTADOR DE NÚMEROS ======")
    numeros = int(input(f"INFORME O {contador + 1} NÚMERO: "))
    

    if numeros < 0 :
        break

    contador += 1


    if numeros % 2 == 0:
        c_numeros_pares.append(numeros)
    else:
        c_numeros_impare.append(numeros)

    media_geral = sum(c_numeros_impare + c_numeros_pares) / contador
    media_pares = sum(c_numeros_pares) / contador 
        
print("====== RESULTADOS =====")
print(f"QUANTIDAE DE NÚMEROS PARES: {len(c_numeros_pares)}")
print(f"MÉDIA: {media_pares}")
print(F"MÉDIA GERAL: {media_geral}")



