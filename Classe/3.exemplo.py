import os
os.system('cls')

from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    e_mail: str
    telefone: str
    endereco: str

    def mostar_dados(self):
        print(f"NOME: {self.nome}")
        print(f"E-MAIL: {self.e_mail}")
        print(f"TELEFONE: {self.telefone}")
        print(f"ENDEREÇO: {self.endereco}")



print("===== SOLICITANDO DADOS =====")
Pessoa1 = Pessoa(nome=(input("DIGITE SEU NOME: ")),
                 e_mail=input("DIGITE SEU E-MAIL: "),
                 telefone=input("DIGITE SEU TELEFONE: "),
                 endereco=input("DIGITE SEU ENDEREÇO: "))

print("\n===== EXIBINDO OS DADOS =====")
Pessoa1.mostar_dados()

