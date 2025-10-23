import os
os.system('cls')

from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    idade: int

    def mostrar_dados(self):
        print("\n===== EXIBINDO DADOS =====")
        print(f"NOME: {self.nome}")
        print(f"IDADE: {self.idade}")

print("===== SOLICITANDO DADOS =====")
pessoa1 = Pessoa(nome=input("DIGITE SEU NOME: "),
                 idade=int(input("DIGITE SUA IDADE: ")))

pessoa2 = Pessoa(nome=input("DIGITE SEU NOME: "),
                 idade=int(input("DIGITE SUA IDADE: ")))

pessoa1.mostrar_dados()
pessoa2.mostrar_dados()
