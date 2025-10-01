import os
os.system('cls')

QUANTIDADE = 4
lista_notas = []
situacao = ""

for i in range(QUANTIDADE):
    nota = float(input(f"INFORME A {i + 1} NOTA: "))
    lista_notas.append(nota)

media = sum(lista_notas) / len(lista_notas)

if media >= 7:
    situacao = "APROVADO"
elif media >= 5:
    situacao = "RECUPERAÇÃO"
else:
    situacao = "REPROVADO"

print("===== RESULTADO =====")
for i in range(QUANTIDADE):
    print(f"NOTA {i + 1}: {lista_notas[i]}")
print(f"MÉDIA: {media:.2f}")
print(f"SITUAÇÃO: {situacao}")

    