import os
os.system('cls')

lista_num = []

for i in range(5):
    numero = int(input(f"INFORM E O {i + 1} NÚMERO: "))
    lista_num.append(numero)


print("===== RESULTADO ======")
for i in range(5):
    print(f"NÚMERO: {lista_num[i]}")
print(f"MAIOR NÚMERO: {max(lista_num)}")
print(f"MENOR NÚMERO: {min(lista_num)}")