import os
os.system('cls')

opcao = int(input("DIGITE UM NÚMERO E DESCUBRA O MÊS CORRESPONDENTE: "))

match opcao:
    case 1:
        print("JANEIRO")
    case 2:
        print("FEVEREIRO")
    case 3:
        print("MARÇO")
    case 4:
        print("ABRIL")
    case 5:
        print("MAIO")
    case 6:
        print("JUNHO")
    case 7:
        print("JULHO")
    case 8:
        print("AGOSTO")
    case 9:
        print("SETEMBRO")
    case 10:
        print("OUTUBRO")
    case 11:
        print("NOVEMBRO")
    case 12:
        print("DEZEMBRO")
    case _:
        print("DIGITE UMA OPÇÃO VÁLIDA!")