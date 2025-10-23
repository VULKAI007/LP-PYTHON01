import os
os.system("cls")

from dataclasses import dataclass

@dataclass
class Cliente:
    nome: str
    e_mail: str
    endereco: str

    def dados_entrega(self):
        print("\n===== DADOS DE ENTREGA =====")
        print(f"NOME: {self.nome}")
        print(f"ENDEREÇO: {self.endereco}")

    def dados_email_marketing(self):
        print("\n===== DADOS DE CONTATO =====")
        print(f"NOME: {self.nome}")
        print(f"E-MAIL: {self.e_mail}")

print("\n======== SOLICITANDO OS DADOS ========")
cliente1 = Cliente(nome= input("DIGITE SEU NOME: "),
                   e_mail=input("DIGITE SEU E-MAIL: "),
                   endereco=input("DIGITE SEU ENDEREÇO: "))

os.system('cls')
cliente1.dados_entrega()
cliente1.dados_email_marketing()
