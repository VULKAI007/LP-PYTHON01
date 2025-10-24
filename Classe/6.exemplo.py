import os
os.system('cls')

from dataclasses import dataclass

@dataclass
class Endereco:
    logradouro: str
    numero: int

@dataclass
class Cliente:
    nome: str
    endereco: Endereco

cliente1 = Cliente(nome="ENZO",
                   endereco=Endereco(
                       logradouro="RUA A",
                       numero=23))

print("===== MOSTAR DADOS DO CLIENTE =====")
print(f"NOME: {cliente1.nome}")
print(f"ENDEREÇO: {cliente1.endereco}")
print(f"NÚMERO: {cliente1.endereco.numero}")