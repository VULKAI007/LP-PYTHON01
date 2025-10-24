import os
os.system('cls')

from dataclasses import dataclass

@dataclass
class Endereco:
    logradouro: str
    numero: int
    cidade: str

@dataclass
class Cliente:
    nome: str
    e_mail: str
    endereco: Endereco

    def mostrar_resultado(self):
        print("===== INFORMAÇÕES DO PERFIL =====")
        print(f"NOMN: {self.nome}")
        print(f"E-MAIL: {self.e_mail}")
        print("\n===== ENDEREÇO =====")
        print(f"LOGRADOURO: {self.endereco.logradouro}\nNÚMERO: {self.endereco.numero}\nCIDADE: {self.endereco.cidade}")

cliente1 = Cliente(nome=input("DIGITE SEU NOME: ").upper(),
                   e_mail=input("DIGITE SEU E-MAIL: ").lower(),
                   endereco=Endereco(logradouro=input("DIGITE SEU LOGRADOURO: "),
                                     numero=int(input("DIGITE O NÚMERO DA SUA CASA: ")),
                                     cidade=input("DIGITE A SUA CIDADE: ")))
os.system('cls')
cliente1.mostrar_resultado()
