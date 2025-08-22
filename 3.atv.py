import os
os.system('cls')

n1 = float(input("INFORME A PRIMEIRA NOTA: "))
n2 = float(input("INFORME A SEGUNDA NOTA: "))
n3 = float(input("INFORME A SEGUNDA NOTA: "))

media = n1 + n2 + n3 / 3

if media >= 7:
    print("O ALUNO ESTA APROVADO: ")
    print(media)
else:
    print("O ALUNO ESTA REPROVADO ")
    print(media)