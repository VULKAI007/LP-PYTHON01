import os
os.system('cls')

from dataclasses import dataclass

@dataclass
class Paciente:
    nome: str
    idade: int
    def exibir_dados(self):
        print(f"NOME: {self.nome}, IDADE: {self.idade}\n")

lista_de_paciente = []
QUANTIDADE_PACIENTE = 2

for i in range(QUANTIDADE_PACIENTE):
    print(f"------ PACIENTE {i +1} ------")
    paciente = Paciente(
        nome= input("DIGITE SEU NOME: "),
        idade=input("DIGITE SUA IDADE: ")
    )
    lista_de_paciente.append(paciente)
    print()#PULAR UMA LINHA

nome_do_arquivo = "dados_paciente.csv"
with open(nome_do_arquivo, "a") as arquivo_pacientes:
    for paciente in lista_de_paciente:
        arquivo_pacientes.write(f"{paciente.nome}, {paciente.idade}\n")
        print("DADOS SALVOS COM SUCESSO. ")

# print("\nEXIBINDO LISTA DE PACIENTES: ")
# for paciente in lista_de_paciente:
#     paciente.exibir_dados()

print("\nEXIBINDO TODOS OS PACIENTES: ")
lista = []
try:

    # "r" - red leitura
    with open(nome_do_arquivo, "r", encoding="utf-8") as arquivo:
        # RECEBE TODOS OS DADOS DO ARQUIVO DE UM SÓ VEZ.
        lista_todos_pacientes = arquivo.readlines()
        for paciente in lista_todos_pacientes:
            nome, idade = paciente.strip().split(",")
            dados_paciente = Paciente(nome=nome, idade=int(idade))
            lista.append(dados_paciente)
    for paciente in lista:
        paciente.exibir_dados()
except FileNotFoundError:
    print("O ARQUIVO NÃO FOI ENCONTRADO. ")
