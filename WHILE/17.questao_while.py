# import os
# os.system("cls")

# # Definindo variávies
# menor_idade = 9999
# maior_idade = 0
# soma_salario = 0
# quantidade_salarios = 0
# mulheres5k = 0

# while True:
#     os.system("cls")
#     print(""""
# Código   |   Descrição
#    1     | Adicionar pessoa
#    2     | Exibir resultados    
#    3     | Sair
# """)

#     opcao = int(input("Digite a opção desejada: "))
#     match opcao:
#         case 1:
#             # Solicitando dados.
#             idade = int(input("Digite a idade: "))
#             sexo = input("Informe o sexo - Use F ou M: ").upper()
#             salario = float(input("Digite o valor salário: "))

#             # Média de salários.
#             quantidade_salarios += 1
#             soma_salario += salario

#             # Maior e menor idades.
#             if idade < menor_idade:
#                 menor_idade = idade

#             if idade > maior_idade:
#                 maior_idade = idade

#             # Quantidade de mulheres com salário >= 5k.
#             if salario >= 5000 and sexo == "F":
#                 mulheres5k += 1

#         case 2:
#             media_salarial = soma_salario / quantidade_salarios if quantidade_salarios != 0 else 0
#             if menor_idade == 9999:
#                 menor_idade = 0
               
#             print("\n= Exibindo resultados =")
#             print(f"Média de salários do grupo: {media_salarial}")
#             print(f"Menor idade do grupo: {menor_idade}")
#             print(f"Maior idade do grupo: {maior_idade}")
#             print(f"Quantidade de mulheres com salário acima de 5 mil: {mulheres5k}")
#             input("Pressione enter para continuar...")
#         case 3:
#             print("Saindo do programa.")
#             input("Pressione enter para sair...")
#             break
#         case _:
#             print("Opção inválida, tente novamente.")
#             input("Pressione enter para continuar...")








lista_nome = []
lista_idade = []
lista_sexo = []
lista_salarios = []
contador = 0
salario_alto = 0

while True:
    print("========== MENU =========")
    print("CÓDIGO | DESCRIÇÃO ")
    print("  1    | Adicionar pessoa")
    print("  2    | Exibir resultados")
    print("  3    | sair")
    opcao = int(input("INFORME O CÓDIGO DA AÇÃO DESEJADA: "))

    


    match opcao:
        case 1:
            print("==== INFORMAÇÕES PARA CADASTRO ====")
            nome = input("INFORME O NOME: ")
            lista_nome.append(nome)
            idade = int(input("INFORME A IDADE: "))
            lista_idade.append(idade)
            sexo = input("INFORME O SEXO(M/F): ").upper()
            lista_sexo.append(sexo)
            salarios = float(input("INFORME O SALÁRIO: "))
            lista_salarios.append(salarios)
            contador += 1
            media = sum(lista_salarios) / contador
            if sexo == "F" and salarios > 5000:
                salario_alto += 1


        case 2:
            print("===== RESULTADO DOS CADASTRADOS =====")
            print(f"NOME DOS CADASTRADOS: {lista_nome}")
            print(f"MEDIA DO SALARIO DOS GRUPOS: {media:.}")
            print(f"MAIOR IDADE DO GRUPO: {max(lista_idade)}")
            print(f"MENOR IDADE DO GRUPO: {min(lista_idade)}")
            print(f"QUANTIDADE DE MULHER QUE GANHAM APARTIR DE 5K: {contador}")
        case 3:
            break
        case _:
            print("INFORME UMA OPÇÃO VÁLIDA! ")


    


