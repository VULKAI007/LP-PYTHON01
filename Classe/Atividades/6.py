import os
os.system('cls' if os.name == 'nt' else 'clear')
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
        print(f"NOME: {self.nome}")
        print(f"E-MAIL: {self.e_mail}")
        print("\n===== ENDEREÇO =====")
        print(f"LOGRADOURO: {self.endereco.logradouro}")
        print(f"NÚMERO: {self.endereco.numero}")
        print(f"CIDADE: {self.endereco.cidade}")
        print("-" * 35)

# Lista global de clientes
lista_cliente = []

def buscar_cliente():
    nome_busca = input("DIGITE O NOME DO CLIENTE QUE DESEJA BUSCAR: ").upper()
    encontrados = [cliente for cliente in lista_cliente if cliente.nome == nome_busca]
    if encontrados:
        for cliente in encontrados:
            cliente.mostrar_resultado()
    else:
        print("CLIENTE NÃO ENCONTRADO!")

while True:
    print("\n====== MENU DE SELEÇÃO ======")
    print("(A) CADASTRAR CLIENTE")
    print("(B) EXIBIR CLIENTES CADASTRADOS")
    print("(C) BUSCAR CLIENTE")
    print("(S) SAIR")
    opcao = input("DIGITE A OPÇÃO QUE DESEJA: ").upper()

    match opcao:
        case "A":
            cliente = Cliente(
                nome=input("DIGITE SEU NOME: ").upper(),
                e_mail=input("DIGITE SEU E-MAIL: ").lower(),
                endereco=Endereco(
                    logradouro=input("DIGITE SEU LOGRADOURO: "),
                    numero=int(input("DIGITE O NÚMERO DA SUA CASA: ")),
                    cidade=input("DIGITE A SUA CIDADE: ")
                )
            )
            lista_cliente.append(cliente)
            print("CLIENTE CADASTRADO COM SUCESSO!")
        
        case "B":
            if not lista_cliente:
                print("NENHUM CLIENTE CADASTRADO!....TENTE CADASTRAR UM CLIENTE.")
            else:
                print("\n=== CLIENTES CADASTRADOS ===")
                for cliente in lista_cliente:
                    cliente.mostrar_resultado()

        case "C":
            buscar_cliente()

        case "S":
            print("SAINDO DO SISTEMA... ATÉ LOGO!")
            break
        
        case _:
            print("OPÇÃO INVÁLIDA! TENTE NOVAMENTE.")














# import os
# os.system('cls')

# from dataclasses import dataclass

# @dataclass
# class Endereco:
#     logradouro: str
#     numero: int
#     cidade: str

# @dataclass
# class Cliente:
#     nome: str
#     e_mail: str
#     endereco: Endereco

#     def mostrar_resultado(self):
#         print("===== INFORMAÇÕES DO PERFIL =====")
#         print(f"NOMN: {self.nome}")
#         print(f"E-MAIL: {self.e_mail}")
#         print("\n===== ENDEREÇO =====")
#         print(f"LOGRADOURO: {self.endereco.logradouro}\nNÚMERO: {self.endereco.numero}\nCIDADE: {self.endereco.cidade}")

# @dataclass
# class Buscador:
#     def buscar_cliente():
#         for id in lista_cliente:
#             print



# lista_cliente = []

# while True:
#     print("====== MENU DE SELEÇÃO ======")
#     print("(A) CADASTRAR CLIENTE")
#     print("(B) EXIBIR CLINTES CADASTRADOS")
#     print("(C) BUSCAR CLIENTE")
#     print("(S) SAIR")
#     opcao = input("DIGITE A OPÇÃO QUE DESEJA: ")

#     match opcao:
#         case "A":
#             cliente = Cliente(nome=input("DIGITE SEU NOME: ").upper(),
#                    e_mail=input("DIGITE SEU E-MAIL: ").lower(),
#                    endereco=Endereco(logradouro=input("DIGITE SEU LOGRADOURO: "),
#                                      numero=int(input("DIGITE O NÚMERO DA SUA CASA: ")),
#                                      cidade=input("DIGITE A SUA CIDADE: ")))
#             lista_cliente.append(cliente)
#         case "B":
#             if lista_cliente == None:
#                 print("NENHUMA CLIENTE CADASTRADO!....TENTE CADASTRAR UM CLIENTE")
#             else:
#                 for cliente in lista_cliente:
#                     print(f"==== clientes ====")
#                     print(lista_cliente[cliente])
#         case "C":
