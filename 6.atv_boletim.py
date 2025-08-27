import os
os.system("cls")

print("---- BOLETIM DO ALUNO ----")
nome = input("DIGITE SEU NOME: ")
n1 = float(input("DIGITE A PRIMEIRA NOTA: "))
n2 = float(input("DIGITE A SEGUNDA NOTA: "))

media = (n1 + n2) / 2

if media >= 9:
    conceito = "A"
elif media >= 7.5:
    conceito = "B"
elif media >= 6:
    ponceito = "C"
elif media >= 4:
    conceito = "D"
elif media < 4:
    conceito = "E"

if conceito == "A" or "B" or "C":
    print("----- FIXA DO ALUNO -----")
    print(f"NOME: ", {nome})
    print(f"MEDIA: ", {media})
    print(f"LETRA: ", {conceito})
    print(f"ALUNO APROVADO")
elif conceito == "D" or "E":
    print("----- FIXA DO ALUNO -----")
    print(f"NOME: ", {nome})
    print(f"MEDIA: ", {media})
    print(f"LETRA: ", {conceito})
    print("RESULTADO: REPROVADO")

