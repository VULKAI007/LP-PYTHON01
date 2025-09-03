import os
os.system('cls')

opcao = int(input("DIGITE UM NÚEMRO DE 1 A 7: "))

if opcao == 2 or 3 or 4 or 5 or 6:
    tipo = "DIA ÚLTIL"
elif opcao == 1 or 7:
    tipo = "FINAL DE SEMANA"


match opcao:
    case 1:
        print(f"DOMINGO / {tipo}")
    case 2:
        print(f"SEGUNDA / {tipo}")
    case 3:
        print(f"TERÇA / {tipo}")
    case 4:
        print(f"QUARTA / {tipo}")
    case 5:
        print(f"QUINTA / {tipo}")
    case 6:
        print(f"SEXTA / {tipo}")
    case 7:
        print(f"SÁBADO / {tipo}")
    case _:
        print("DIGITE UM OPÇÃO VÁLIDA!")