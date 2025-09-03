import os
os.system('cls')



print("======= CALCULADORA DE PESO =======")
nome = input("DIGITE SEU NOME: ")
sexo = input("DIGITE 'M' PARA HOMEM E 'F' PARA MULHER ").strip().upper()
altura = float(input("INFORME SUA ALTURA: "))

match sexo:
    case "M":
        peso_ideal = (72.7 * altura)-58
        print("====== RESULTADO =====")
        print(f"NOME: {nome}")
        print(f"PESO IDEAL: {peso_ideal:.2f} KG")
    case "F":
        peso_ideal = (62.1 * altura)-44.7
        print("====== RESULTADO =======")
        print(f"NOME: {nome}")
        print(f"PESO IDEAL: {peso_ideal:.2f} KG")
    case _:
        print("DIGITE UM GÊNERO DISPONÍVEL")