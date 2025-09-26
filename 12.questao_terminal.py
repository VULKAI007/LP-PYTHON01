import os
os.system('cls')
notas = []

for i in range(3):
    nota = float(input(f"INFORME A {i + 1} NOTA: "))
    notas.append(nota)
    if nota < 0 or nota > 10:
        nota = float(input(f"INFORME A {i + 1} NOTA: "))
        notas.append(nota)