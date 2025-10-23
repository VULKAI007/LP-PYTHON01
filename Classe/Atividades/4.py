import os
os.system("cls")

from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    e_mail: str
    endereco: str

    def mostras_dados(self):
        print(f"NOME: {self.nome}")
        print(f"E-MAIL: {self.e_mail}")
        print(f"ENDEREÇO: {self.endereco}")

    def mostrar_somente_nome(self):
        print("===== SOMENTE NOME =====")
        print(f"NOME: {self.nome}")


# CRIANDO UMA LISTA(VETOR)
lista_pessoas = []
print("\n")
for i in range(2):
    print("======= SOLICITANDO DADOS DA PESSOA  =======")
    pessoa = Pessoa(nome=input("DIGITE SEU NOME: "),
                    e_mail=input("DIGITE SEU E-MAIL: "),
                    endereco=input("DIGITE SEU ENDEREÇO: "))
    lista_pessoas.append(pessoa)

print("\n====== EXIBINDO DADOS GERAIS =======")
for pessoa in lista_pessoas:
    pessoa.mostras_dados()

print("\n===== EXIBINDO DADOS ESPECÍFICOS =====")
for pessoa in lista_pessoas:
    pessoa.mostrar_somente_nome()

