import os
os.system('cls')

print("------ QUAL OPERAÇÃO DESEJA REALIZAR ------")
print("+ - * /")
ope = input("DIGITE A OPERAÇÃO: ")
n1 = int(input("DIGITE A PRIMEIRO NÚMERO QUE DESEJA CALCULAR: "))
n2 = int(input("DIGITE O SEGUNDO NÚMERO QUE DESEJA CALCULAR: "))

match ope:
    case "+":
        print("SOMA ESCOLHIDA!")
        print("RESULTADO: ", n1 + n2)
    case "-":
        print("SUBTRAÇÃO ESCOLHIDA!")
        print("RESULTADO: ", n1 - n2)
    case "*":
        print("MULTIPLICAÇÃO ESCOLHIDA!")
        print("RESULTADO: ", n1 * n2)
    case "/":
        print("DIVISÃO ESCOLHIDA!")
        print("RESULTADO: ", n1 / n2)
    case _:
        print("OPÇÃO INVÁLIDA!!")

print("FIM")















""""

dia = int(input("DIGITE UM NÚNERO PARA O DIA DA SEMANA: "))

match dia:
    case 1:
        print("DOMINGO!")
    case 2:
        print('SEGUNDA-FEIRA')
    case 3:
        print("TERÇA-FEIRA")
    case 4:
        print("QUARTA-FEIRA")
    case 5:
        print("QUINTA-FEIRA")
    case 6:
        print("SEXTA-FEIRA")
    case 7:
        print("SÁBADO!")
    case _:
        print("OPÇÃO INVÁLIDA.")

print("FIM")

"""