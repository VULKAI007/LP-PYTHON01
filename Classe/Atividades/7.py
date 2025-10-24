import os
os.system("cls")

from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    idade: int
    peso: float
    altura: float

    def mostras_dados(self):
        print(f"NOME: {self.nome}")
        print(f"IDADE: {self.idade}")
        print(f"PESO: {self.peso}")
        print(f"ALTURA: {self.altura}")


# CRIANDO UMA LISTA(VETOR)
lista_pessoas = []
print("\n")
for i in range(4):
    print("======= SOLICITANDO DADOS DA PESSOA  =======")
    pessoa = Pessoa(nome=input("DIGITE SEU NOME: "),
                    idade=int(input("DIGITE SEU IDADE: ")),
                    peso=float(input("DIGITE SEU PESO: ")),
                    altura=float(input("DIGITE SUA ALTURA EM CM: ")))
    lista_pessoas.append(pessoa)

cont = 0
print("\n====== EXIBINDO DADOS GERAIS =======")
for pessoa in lista_pessoas:
    cont += 1
    print(f"\n==== PESSOA {cont}° ====")
    pessoa.mostras_dados()