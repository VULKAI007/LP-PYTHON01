import os
os.system('cls')

from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    idade: int
    altura: float
    peso: float

print("SOLICITANDO OS DADOS DA PESSOA. ")
pessoa1 = Pessoa(nome=input("DIGITE SEU NOME: "),
                 idade=int(input("DIGITE SUA IDADE: ")),
                 altura=float(input('DIGITE SUA ALTURA: ')),
                 peso=float(input("DIGITE SEU PESO: ")))

print("EXIBINDO DADOS DA PESSOA")
print(f"NOME: {pessoa1.nome}\nidade: {pessoa1.idade}\nALTURA: {pessoa1.altura} M."
      f"\nPESO: {pessoa1.peso} KG")





