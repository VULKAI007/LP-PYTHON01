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

@dataclass
class Buscador:
    def buscar_cliente():
        for id in lista_cliente:
            print



lista_cliente = []

while True:
    print("====== MENU DE SELEÇÃO ======")
    print("(A) CADASTRAR CLIENTE")
    print("(B) EXIBIR CLINTES CADASTRADOS")
    print("(C) BUSCAR CLIENTE")
    print("(S) SAIR")
    opcao = input("DIGITE A OPÇÃO QUE DESEJA: ")

    match opcao:
        case "A":
            cliente = Cliente(nome=input("DIGITE SEU NOME: ").upper(),
                   e_mail=input("DIGITE SEU E-MAIL: ").lower(),
                   endereco=Endereco(logradouro=input("DIGITE SEU LOGRADOURO: "),
                                     numero=int(input("DIGITE O NÚMERO DA SUA CASA: ")),
                                     cidade=input("DIGITE A SUA CIDADE: ")))
            lista_cliente.append(cliente)
        case "B":
            if lista_cliente == None:
                print("NENHUMA CLIENTE CADASTRADO!....TENTE CADASTRAR UM CLIENTE")
            else:
                for cliente in lista_cliente:
                    print(f"==== clientes ====")
                    print(lista_cliente[cliente])
        case "C":
