import os
os.system('cls')

from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    e_mail: str
    telefone: str
    endereco: str

print("===== SOLICITANDO DADOS =====")
Pessoa1 = Pessoa(nome=(input("DIGITE SEU NOME: ")),
                 e_mail=input("DIGITE SEU E-MAIL: "),
                 telefone=input("DIGITE SEU TELEFONE: "),
                 endereco=input("DIGITE SEU ENDEREÇO: "))

print("\n===== EXIBINDO OS DADOS =====")
print(f"NOME: {Pessoa1.nome}")
print(f"E-MAIL: {Pessoa1.e_mail}")
print(f"TELEFONE: {Pessoa1.telefone}")
print(f"ENDEREÇO: {Pessoa1.endereco}")
