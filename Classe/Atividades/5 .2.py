import os
os.system('cls')

from dataclasses import dataclass

@dataclass
class Endereco:
    logradouro: str
    numero: int


@dataclass
class Pessoa:
    nome: str
    idade: int
    endereco: Endereco

pessoa1 = Pessoa(nome=input("DIGITE SEU NOME: ").upper(),
                 idade= int(input("DIGITE SUA IDADE: ")),
                 endereco= Endereco(logradouro=input("INFORME SEU LOGRADOURO: "),
                                    numero= int(input("DIGITE SEU NÚMERO: "))))


print("===== INFORMAÇÕES DO PERFIL =====")
print(f"NOMN: {pessoa1.nome}")
print(f"IDADE: {pessoa1.idade}")
print("\n===== ENDEREÇO =====")
print(f"LOGRADOURO: {pessoa1.endereco.logradouro}\nNÚMERO: {pessoa1.endereco.numero}\n")

