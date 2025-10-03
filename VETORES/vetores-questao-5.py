import os
os.system('cls')

cont = 0
lista_numero = []

while True:

    numero = float(input(f"INFORME O {cont + 1}ª NÚMERO: "))
    cont += 1
    
    if numero <= 0:
        numero = 0
        lista_numero.append(numero)
    else:
        lista_numero.append(numero)
    if cont >= 5:
        break
print("====== RESPOSTA =====")
for i, numero in enumerate(lista_numero):
    print(f"{i+1}º NÚMERO: {numero}")




