import os
os.system('cls')

notas = []

for i in range(3):
    nota = float(input(f"DIGITE A {1+i} NOTA: "))
    notas.append(nota)
media = sum(notas) / len(notas)

print("===== RESULTADO =====")
for i in range(3):
    print(f"NOTAS: {notas[i]}")
print(f"MEDIA: {media}")



