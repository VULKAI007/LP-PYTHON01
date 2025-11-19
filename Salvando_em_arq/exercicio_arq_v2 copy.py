import os
os.system('cls')

from dataclasses import dataclass

@dataclass
class Funcionario:
    nome: str
    data_nascimento: str
    rg: str
    cpf: str

    def exibir_dados(self):
        print(f"NOME: {self.nome}, DATA DE NASCIMENTO: {self.data_nascimento}, RG: {self.rg}, CPF: {self.cpf}")
    
lista_de_funcionario = []
QUANTIDADE_PACIENTE = 2


for i in range(QUANTIDADE_PACIENTE):
    print(f"------ PACIENTE {i +1} ------")
    funcionario = Funcionario(
        nome= input("DIGITE SEU NOME: "),
        data_nascimento=input("DIGITE SUA DATA DE NASCIMENTO "),
        rg=input("DIGITE SEU RG: "),
        cpf=input("DIGITE SEU CPF: "),
    )
    lista_de_funcionario.append(funcionario)
    print()#PULAR UMA LINHA

nome_do_arquivo = "dados_funcionario.csv"
with open(nome_do_arquivo, "a") as arquivo_funcionario:
    for funcionario in lista_de_funcionario:
        arquivo_funcionario.write(f"{funcionario.nome}, {funcionario.idade}\n")
        print("DADOS SALVOS COM SUCESSO. ")

