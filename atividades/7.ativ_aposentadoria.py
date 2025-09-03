import os
os.system('cls')

print("----- REQUERIMENTO DE APOSENTADORIA -----")
rf = input("DIGITE SEU REGISTRO DE FUNCIONÁRIO: ")
ano = int(input("DIGITE SEU ANO DE NASCIMENTO: "))
t_servico = float(input("DIGITE O SEU TEMPO TRABALHADO EM ANOS: "))

idade = 2025 - ano

if idade >= 65 or t_servico >= 30:
    print("----- INFORMAÇÕES DO FUNCIONÁRIO -----")
    print("REGISTRO DO DUNCIONÁRIO: ", idade)
    print("IDADE: ", idade)
    print("TEMPO DE SERVIÇO: ", t_servico)
    print("REQUERER A APOSENTADORIA")
else:
    print("----- INFORMAÇÕES DO FUNCIONÁRIO -----")
    print("REGISTRO DO DUNCIONÁRIO: ", idade)
    print("IDADE: ", idade)
    print("TEMPO DE SERVIÇO: ", t_servico)
    print("REQUERER A APOSENTADORIA")

