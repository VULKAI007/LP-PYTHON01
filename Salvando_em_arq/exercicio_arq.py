import os
os.system('cls')

from dataclasses import dataclass

@dataclass
class Paciente:
    nome: str
    idade: int
    peso: float
    altura: float
    cpf: str

    def exibir_dados(self):
        print("===== EXIBINDO DADOS =====")
        print(f"NOME: {self.nome}, IDADE: {self.idade}, PESO: {self.peso}, ALTURA: {self.altura}, {self.cpf}")
        print("============================")

lista_de_paciente = []
QUANTIDADE_PACIENTE = 1

for i in range(QUANTIDADE_PACIENTE):
    paciente = Paciente(
        nome=input("DIGITE SEU NOME: "),
        idade=int(input("DIGITE SUA IDADE: ")),
        peso=float(input("DIGITE SEU PESO (KG): ")),
        altura=float(input("DIGITE SUA AULTURA:")),
        cpf=input("DIGITE SEU CPF: ")

    )
    lista_de_paciente.append(paciente)
    print()#PULAR UMA LINHA

nome_do_arquivo = "teste_paciente.csv"
with open(nome_do_arquivo, "a") as arquivo_pacientes:
    for paciente in lista_de_paciente:
        arquivo_pacientes.write(f"{paciente.nome}, {paciente.idade}, {paciente.peso}, {paciente.altura}"
                                f"{paciente.cpf}")
    print("DADOS SALVOS COM SUCESSO. ")

# print("\nEXIBINDO LISTA DE PACIENTES: ")
# for paciente in lista_de_paciente:
#     paciente.exibir_dados()

print("\nEXIBINDO TODOS OS PACIENTES: ")
try:
    # "r" - red - leitura
    with open(nome_do_arquivo, "r") as arquivo:
        # RECEBE TODOS OS DADOS DO ARQUIVO DE UMA SÓ VEZ
        lista_todos_pacientes = arquivo.readlines()
        for paciente in lista_todos_pacientes:
            print(f"- {paciente.strip()}")
except FileExistsError:
    print("O ARQUIVO NÃO FOI ENCONTRADO. ")