import os
os.system('cls')

from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    idade: int
    altura: float
    peso: float

pessoa1 = Pessoa("ALICE", 30, 182, 72)

print("EXIBINDO DADOS DA PESSOA")
print(f"NOME: {pessoa1.nome}\nidade: {pessoa1.idade}\nALTURA: {pessoa1.altura} M.\nPESO: {pessoa1.peso} KG")
