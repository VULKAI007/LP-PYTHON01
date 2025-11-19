import os
os.system('cls')

from dataclasses import dataclass

@dataclass
class Paciente:
    nome: str
    idade: int
    def exibir_dados(self):
        print(f"NOME: {self.nome} \n{self.idade}")

lista_de_paciente = []
QUANTIDADE_PACIENTE = 2

for i in range(QUANTIDADE_PACIENTE):
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

print("\nEXIBINDO LISTA DE PACIENTES: ")
for paciente in lista_de_paciente:
    paciente.exibir_dados()
