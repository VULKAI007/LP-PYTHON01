import os
os.system('cls')
from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    cpf: str
    telefone: str

    def mostras_dados(self):
        print(f"NOME: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"TELEFONE: {self.telefone}")

    def dados_sms_marketing(self):
        print("===== SOMENTE TELEFONE =====")
        print(f"TELEFONE: {self.telefone}")


# CRIANDO UMA LISTA(VETOR)
lista_pessoas = []
print("\n")
for i in range(3):
    print("======= SOLICITANDO DADOS DA PESSOA  =======")
    pessoa = Pessoa(nome=input("DIGITE SEU NOME: "),
                    cpf=input("DIGITE SEU CPF: "),
                    telefone=input("DIGITE SEU TELEFONE: "))
    lista_pessoas.append(pessoa)

os.system('cls')
print("\n====== EXIBINDO DADOS GERAIS =======")
for pessoa in lista_pessoas:
    pessoa.mostras_dados()
    print('\n')

print("\n===== EXIBINDO DADOS ESPECÍFICOS =====")
for pessoa in lista_pessoas:
    pessoa.dados_sms_marketing()

