import os
os.system('cls')

list_salario = []
list_filho = []
media_salario = 0
media_filhos = 0
cont = 0
numeros_filhos = 0

while True:
    print("========== MENU =========")
    print("CÓDIGO | DESCRIÇÃO ")
    print("  1    | Adicionar Família")
    print("  2    | sair e Exibir resultados")
    opcao = int(input("INFORME O CÓDIGO DA AÇÃO DESEJADA: "))
    match opcao:
        case 1:
            salario = float(input("INFORME O SALÁRIO DA SUA FAMÍLIA: "))
            list_salario.append(salario)
            numeros_filhos = int(input("INFORME O NÚMERO DE FILHOS: "))
            list_filho.append(numeros_filhos)
            cont += 1
            os.system('cls')
        case 2:
            media_salario = sum(list_salario) / cont
            media_filhos = sum(list_filho) / cont

            print("====== RESULTADO ======")
            print(f"TOTAL DE FAMILIAS {cont}")
            print(f"MEDIA DO SALÁRIO: {media_salario}")
            print(f"MEDIA DO FILHOS: {media_filhos}")
            print(f"MAIOR SALÁRIO: {max(list_salario)}")
            print(f"MENOR SALÁRIO: {min(list_salario)}")
            break
        case _:
            print("INFORME UMA OPÇÃO VÁLIDA!")
            print("PRESS ENTER FOR CONTINUE...")