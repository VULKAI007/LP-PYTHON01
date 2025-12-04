# import os
# import time
# from dataclasses import dataclass

# os.system('cls || clear')  # Limpar terminal

# lista_clientes = []
# lista_produtos = []


# @dataclass
# class Endereco:
#     logradouro: str
#     numero: int
#     cidade: str
#     estado: str


# @dataclass
# class Produto:
#     nome: str
#     quantidade: int
#     lote: str
#     validade:  str

#     def mostrar_produtos(self):
#         print('====== PRODUTOS CADASTRADOS ======')
#         print(f"\nNome: {self.nome}")
#         print(f"Quantidade: {self.quantidade}")
#         print(f"Lote: {self.lote}")
#         print(f"Validade: {self.validade}")


# @dataclass
# class Cliente:
#     nome: str
#     email: str
#     telefone: str
#     endereco: Endereco

#     def mostrar_dados(self):
#         print("===== EXIBINDO DADOS DO CLIENTE =====")
#         print(f'\nNome: {self.nome}')
#         print(f'E-mail: {self.email}')
#         print(f'Telefone: {self.telefone}')
#         print(f"------ ENDEREÇO ------")
#         print(f"LOGRADOURO: {self.endereco.logradouro}")
#         print(f"NÚMERO: {self.endereco.numero}")
#         print(f"CIDADE: {self.endereco.cidade}")
#         print(f"ESTADO: {self.endereco.estado}")

# # VERIFICAR SE A LISTA CLIENTES ESTA VAZIA
# def lista_esta_vazia(lista_clientes):
#     if not lista_clientes:
#         print("\nNÃO HÁ CLIENTES CADASTRADOS")
#         return True
#     return False

# # VERIFICA SE A LISTA PRODUTOS ESTA VAZIA
# def lista_vazia_produto(lista_produtos):
#     if not lista_produtos:
#         print("\nNÃO HÁ PRODUTOS CADASTRADOS")
#         return True
#     return False


# # ADICIONAR CLIENTE
# def adicionar_cliente(lista_clientes):
#     print("\n====== ADICIONAR NOVO CLIENTE ======")
#     nome = input("DIGITE O NOME: ")
#     email = input("DIGITE O EMAIL: ")
#     telefone = input("DIGITE O TELEFONE: ")

#     print("------- ENDEREÇO -------")
#     logradouro = input("DIGITE O LOGRADOURO: ")
#     numero = int(input("DIGITE O NÚMERO: "))
#     cidade = input("DIGITE A CIDADE: ")
#     estado = input("DIGITE O ESTADO: ")

#     novo_cliente = Cliente(
#         nome=nome,
#         email=email,
#         telefone=telefone,
#         endereco=Endereco(
#             logradouro=logradouro,
#             numero=numero,
#             cidade=cidade,
#             estado=estado
#         )
#     )

#     lista_clientes.append(novo_cliente)
#     print(f"\nCLIENTE {nome} ADICIONADO COM SUCESSO!")


# # ADICIONAR PRODUTO
# def adicionar_produto(lista_produtos):
#     print("\n====== ADICIONAR NOVO PRODUTO ======")
#     nome = input("DIGITE O NOME: ")
#     quantidade = int(input("DIGITE A QUANTIDADE: "))
#     lote = input("INFORME O LOTE: ")
#     validade = input("INFORME A VALIDADE: ")


#     novo_produto = Produto(
#         nome=nome,
#         quantidade=quantidade,
#         lote=lote,
#         validade=validade
        
#     )

#     lista_produtos.append(novo_produto)
#     print(f"\nPRODUTO {nome} ADICIONADO COM SUCESSO!")


# # ENCONTRAR CLIENTE POR NOME
# def encontrar_cliente_por_nome(lista_clientes, nome_buscar):
#     nome_buscar_lower = nome_buscar.lower()
#     for cliente in lista_clientes:
#         if cliente.nome.lower() == nome_buscar_lower:
#             return cliente
#     return None

# # ENCONTRAR PRODUTO POR NOME
# def encontrar_produto_por_nome(lista_produtos, nome_buscar_prod):
#     nome_buscar_prod_lower = nome_buscar_prod.lower()
#     for produto in lista_produtos:
#         if produto.nome.lower() == nome_buscar_prod_lower:
#             return produto
#     return None



# # MOSTRAR TODOS OS CLIENTES
# def mostrar_todos_clientes(lista_clientes):
#     if lista_esta_vazia(lista_clientes):
#         return
#     print("\n======= LISTA DE CLIENTES ======")
#     for cliente in lista_clientes:
#         cliente.mostrar_dados()

# # MOSTRAR TODOS OS PRODUTOS
# def mostrar_todos_produtos(lista_produtos):
#     if lista_vazia_produto(lista_produtos):
#         return
#     print("\n======= LISTA DE PRODUTOS ======")
#     for produto in lista_produtos:
#         produto.mostrar_produtos()



# # ATUALIZAR CLIENTE
# def atualizar_cliente(lista_clientes):
#     if lista_esta_vazia(lista_clientes):
#         return
    
#     mostrar_todos_clientes(lista_clientes)
#     print("------ ATUALIZAR DADOS DO CLIENTE ------")
#     nome_buscar = input("\nDIGITE O NOME DO CLIENTE: ")
#     cliente = encontrar_cliente_por_nome(lista_clientes, nome_buscar)

#     if cliente:
#         print("\nCLIENTE ENCONTRADO.")
#         print("\nDIGITE NOVOS DADOS OU DEIXE EM BRANCO PARA MANTER:")

#         novo_nome = input(f"NOME ATUAL: {cliente.nome}\nNOVO NOME: ")
#         novo_email = input(f"EMAIL ATUAL: {cliente.email}\nNOVO EMAIL: ")
#         novo_tel = input(f"TELEFONE ATUAL: {cliente.telefone}\nNOVO TELEFONE: ")

#         novo_logradouro = input(f"LOGRADOURO ATUAL: {cliente.endereco.logradouro}\nNOVO LOGRADOURO: ")
#         novo_numero = input(f"NÚMERO ATUAL: {cliente.endereco.numero}\nNOVO NÚMERO: ")
#         novo_cidade = input(f"CIDADE ATUAL: {cliente.endereco.cidade}\nNOVA CIDADE: ")
#         novo_estado = input(f"ESTADO ATUAL: {cliente.endereco.estado}\nNOVO ESTADO: ")

#         if novo_nome: cliente.nome = novo_nome
#         if novo_email: cliente.email = novo_email
#         if novo_tel: cliente.telefone = novo_tel
#         if novo_logradouro: cliente.endereco.logradouro = novo_logradouro
#         if novo_numero: cliente.endereco.numero = int(novo_numero)
#         if novo_cidade: cliente.endereco.cidade = novo_cidade
#         if novo_estado: cliente.endereco.estado = novo_estado

#         print("\nDADOS ATUALIZADOS COM SUCESSO!")
#     else:
#         print("\nCLIENTE NÃO ENCONTRADO.")


# # ATUALIZAR PRODUTO
# def atualizar_produtos(lista_produtos):
#     if lista_vazia_produto(lista_produtos):
#         return
    
#     mostrar_todos_produtos(lista_produtos)
#     print("------ ATUALIZAR DADOS DO PRODUTOS ------")
#     nome_buscar_prod = input("\nDIGITE O NOME DO PRODUTO: ")
#     produto = encontrar_produto_por_nome(lista_produtos, nome_buscar_prod)

#     if produto:
#         print("\nPRODUTO ENCONTRADO.")
#         print("\nDIGITE NOVOS DADOS OU DEIXE EM BRANCO PARA MANTER:")

#         novo_nome_prod = input(f"NOME ATUAL: {produto.nome}\nNOVO NOME: ")
#         novo_quantidade = input(f"QUANTIDADE ATUAL: {produto.quantidade}\nNOVA QUANTIDADE: ")
#         novo_lote = input(f"LOTE ATUAL: {produto.lote}\nNOVO LOTE: ")
#         novo_validade = input(f"VALIDADE ATUAL: {produto.validade}\nNOVA VALIDADE: ")

#         if novo_nome_prod: produto.nome = novo_nome_prod
#         if novo_quantidade: produto.quantidade = novo_quantidade
#         if novo_lote: produto.lote = novo_lote
#         if novo_validade: produto.validade = novo_validade

#         print("\nDADOS ATUALIZADOS COM SUCESSO!")
#     else:
#         print("\nPRODUTO NÃO ENCONTRADO.")

# # EXCLUIR CLIENTE
# def excluir_cliente(lista_clientes):
#     if lista_esta_vazia(lista_clientes):
#         return
    
#     mostrar_todos_clientes(lista_clientes)
#     nome_buscar = input('\nDigite o nome do cliente que deseja excluir: ')
#     cliente = encontrar_cliente_por_nome(lista_clientes, nome_buscar)

#     if cliente:
#         lista_clientes.remove(cliente)
#         print(f'\nCLIENTE {cliente.nome} EXCLUÍDO COM SUCESSO!')
#     else:
#         print('\nCLIENTE NÃO ENCONTRADO.')


# # EXCLUIR PRODUTO
# def excluir_produto(lista_produtos):
#     if lista_esta_vazia(lista_produtos):
#         return
    
#     mostrar_todos_produtos(lista_produtos)
#     nome_buscar_prod = input('\nDIGITE O NOME DO PRODUTO QUE DESEJA EXCLUIR: ')
#     produto = encontrar_produto_por_nome(lista_produtos, nome_buscar_prod)

#     if produto:
#         lista_produtos.remove(produto)
#         print(f'\nPRODUTO {produto.nome} EXCLUÍDO COM SUCESSO!')
#     else:
#         print('\nPRODUTO NÃO ENCONTRADO.')


# # MENU PRINCIPAL
# while True:

#     print("====== EMPRESA MAMÃO COM AÇÚCAR ======")
#     print("(A) GERENCIAR CLIENTES")
#     print("(B) GERENCIAR PRODUTOS")
#     print("(S) SAIR")
#     escolha =input("\nR:").upper()


#     if escolha == 'A':

#         while True:


#             print("""
#         ===== GERENCIADOR DE CLIENTES =====
#         1 - ADICIONAR
#         2 - MOSTRAR TODOS
#         3 - ATUALIZAR
#         4 - EXCLUIR
#         0 - SAIR

#         """)

#             try:
#                 opcao = int(input('Digite uma opção: '))
#             except ValueError:
#                 print('\nEntrada inválida. Digite um número.')
#                 time.sleep(2)
#                 os.system('cls || clear')
#                 continue

#             match opcao:
#                 case 1:
#                     adicionar_cliente(lista_clientes)
#                 case 2:
#                     mostrar_todos_clientes(lista_clientes)
#                 case 3:
#                     atualizar_cliente(lista_clientes)
#                 case 4:
#                     excluir_cliente(lista_clientes)
#                 case 0:
#                     print('\nSaindo do programa...')
#                     break
#                 case _:
#                     print('\nOpção inválida!')

#             if opcao != 0:
#                 time.sleep(2)
#                 os.system('cls || clear')

#     elif escolha == 'B':


#         while True:

#             print("""
#         ===== GERENCIADOR DE PRODUTOS =====
#         1 - ADICIONAR
#         2 - MOSTRAR TODOS
#         3 - ATUALIZAR
#         4 - EXCLUIR
#         0 - SAIR

#         """)

#             try:
#                 opcao_prod = int(input('Digite uma opção: '))
#             except ValueError:
#                 print('\nEntrada inválida. Digite um número.')
#                 time.sleep(2)
#                 os.system('cls || clear')
#                 continue

#             match opcao_prod:
#                 case 1:
#                     adicionar_produto(lista_produtos)
#                 case 2:
#                     mostrar_todos_produtos(lista_produtos)
#                 case 3:
#                     atualizar_produtos(lista_produtos)
#                 case 4:
#                     excluir_produto(lista_produtos)
#                 case 0:
#                     print('\nSaindo do programa...')
#                     break
#                 case _:
#                     print('\nOpção inválida!')

#             if opcao != 0:
#                 time.sleep(2)
#                 os.system('cls || clear')
#     elif escolha == 'S':
#         print('\nSaindo do programa...')
#         break


#     if escolha != 'S':
#         time.sleep(2)
#         os.system('cls || clear')
    

import os
import time
from dataclasses import dataclass

os.system('cls || clear')  # Limpar terminal

lista_clientes = []
lista_produtos = []

@dataclass
class Endereco:
    logradouro: str
    numero: int
    cidade: str
    estado: str

@dataclass
class Produto:
    nome: str
    quantidade: int
    lote: str
    validade: str

    def mostrar_dados(self):
        print('====== PRODUTO ======')
        print(f"Nome: {self.nome}")
        print(f"Quantidade: {self.quantidade}")
        print(f"Lote: {self.lote}")
        print(f"Validade: {self.validade}")

@dataclass
class Cliente:
    nome: str
    email: str
    telefone: str
    endereco: Endereco

    def mostrar_dados(self):
        print("===== CLIENTE =====")
        print(f"Nome: {self.nome}")
        print(f"E-mail: {self.email}")
        print(f"Telefone: {self.telefone}")
        print("------ ENDEREÇO ------")
        print(f"Logradouro: {self.endereco.logradouro}")
        print(f"Número: {self.endereco.numero}")
        print(f"Cidade: {self.endereco.cidade}")
        print(f"Estado: {self.endereco.estado}")

# ==================== Funções auxiliares ====================
def lista_esta_vazia(lista):
    return not lista

def verificar_lista_clientes(lista_clientes):
    if not lista_clientes:
        print("\nNÃO HÁ CLIENTES CADASTRADOS")
        return True
    return False

def verificar_lista_produtos(lista_produtos):
    if not lista_produtos:
        print("\nNÃO HÁ PRODUTOS CADASTRADOS")
        return True
    return False

# ==================== Funções de Cliente ====================
def adicionar_cliente(lista_clientes):
    print("\n====== ADICIONAR NOVO CLIENTE ======")
    nome = input("Digite o nome: ")
    email = input("Digite o email: ")
    telefone = input("Digite o telefone: ")
    print("------- ENDEREÇO -------")
    logradouro = input("Digite o logradouro: ")
    numero = int(input("Digite o número: "))
    cidade = input("Digite a cidade: ")
    estado = input("Digite o estado: ")

    novo_cliente = Cliente(nome, email, telefone, Endereco(logradouro, numero, cidade, estado))
    lista_clientes.append(novo_cliente)
    print(f"\nCLIENTE {nome} ADICIONADO COM SUCESSO!")

def encontrar_cliente_por_nome(lista_clientes, nome_buscar):
    for cliente in lista_clientes:
        if cliente.nome.lower() == nome_buscar.lower():
            return cliente
    return None

def mostrar_todos_clientes(lista_clientes):
    if verificar_lista_clientes(lista_clientes):
        return
    print("\n======= LISTA DE CLIENTES ======")
    for cliente in lista_clientes:
        cliente.mostrar_dados()

def atualizar_cliente(lista_clientes):
    if verificar_lista_clientes(lista_clientes):
        return
    mostrar_todos_clientes(lista_clientes)
    nome_buscar = input("\nDigite o nome do cliente: ")
    cliente = encontrar_cliente_por_nome(lista_clientes, nome_buscar)
    if cliente:
        print("\nCliente encontrado. Deixe em branco para manter o valor atual.")
        novo_nome = input(f"Nome atual ({cliente.nome}): ")
        novo_email = input(f"Email atual ({cliente.email}): ")
        novo_tel = input(f"Telefone atual ({cliente.telefone}): ")
        novo_logradouro = input(f"Logradouro atual ({cliente.endereco.logradouro}): ")
        novo_numero = input(f"Número atual ({cliente.endereco.numero}): ")
        novo_cidade = input(f"Cidade atual ({cliente.endereco.cidade}): ")
        novo_estado = input(f"Estado atual ({cliente.endereco.estado}): ")

        if novo_nome: cliente.nome = novo_nome
        if novo_email: cliente.email = novo_email
        if novo_tel: cliente.telefone = novo_tel
        if novo_logradouro: cliente.endereco.logradouro = novo_logradouro
        if novo_numero: cliente.endereco.numero = int(novo_numero)
        if novo_cidade: cliente.endereco.cidade = novo_cidade
        if novo_estado: cliente.endereco.estado = novo_estado

        print("\nDados atualizados com sucesso!")
    else:
        print("\nCliente não encontrado.")

def excluir_cliente(lista_clientes):
    if verificar_lista_clientes(lista_clientes):
        return
    mostrar_todos_clientes(lista_clientes)
    nome_buscar = input('\nDigite o nome do cliente que deseja excluir: ')
    cliente = encontrar_cliente_por_nome(lista_clientes, nome_buscar)
    if cliente:
        lista_clientes.remove(cliente)
        print(f'\nCliente {cliente.nome} excluído com sucesso!')
    else:
        print('\nCliente não encontrado.')

# ==================== Funções de Produto ====================
def adicionar_produto(lista_produtos):
    print("\n====== ADICIONAR NOVO PRODUTO ======")
    nome = input("Digite o nome: ")
    quantidade = int(input("Digite a quantidade: "))
    lote = input("Informe o lote: ")
    validade = input("Informe a validade: ")

    novo_produto = Produto(nome, quantidade, lote, validade)
    lista_produtos.append(novo_produto)
    print(f"\nProduto {nome} adicionado com sucesso!")

def encontrar_produto_por_nome(lista_produtos, nome_buscar):
    for produto in lista_produtos:
        if produto.nome.lower() == nome_buscar.lower():
            return produto
    return None

def mostrar_todos_produtos(lista_produtos):
    if verificar_lista_produtos(lista_produtos):
        return
    print("\n======= LISTA DE PRODUTOS ======")
    for produto in lista_produtos:
        produto.mostrar_dados()

def atualizar_produto(lista_produtos):
    if verificar_lista_produtos(lista_produtos):
        return
    mostrar_todos_produtos(lista_produtos)
    nome_buscar = input("\nDigite o nome do produto: ")
    produto = encontrar_produto_por_nome(lista_produtos, nome_buscar)
    if produto:
        print("\nProduto encontrado. Deixe em branco para manter o valor atual.")
        novo_nome = input(f"Nome atual ({produto.nome}): ")
        nova_quantidade = input(f"Quantidade atual ({produto.quantidade}): ")
        novo_lote = input(f"Lote atual ({produto.lote}): ")
        nova_validade = input(f"Validade atual ({produto.validade}): ")

        if novo_nome: produto.nome = novo_nome
        if nova_quantidade: produto.quantidade = int(nova_quantidade)
        if novo_lote: produto.lote = novo_lote
        if nova_validade: produto.validade = nova_validade

        print("\nDados atualizados com sucesso!")
    else:
        print("\nProduto não encontrado.")

def excluir_produto(lista_produtos):
    if verificar_lista_produtos(lista_produtos):
        return
    mostrar_todos_produtos(lista_produtos)
    nome_buscar = input('\nDigite o nome do produto que deseja excluir: ')
    produto = encontrar_produto_por_nome(lista_produtos, nome_buscar)
    if produto:
        lista_produtos.remove(produto)
        print(f'\nProduto {produto.nome} excluído com sucesso!')
    else:
        print('\nProduto não encontrado.')


while True:
    os.system('cls || clear')
    print("====== EMPRESA MAMÃO COM AÇÚCAR ======")
    print("(A) GERENCIAR CLIENTES")
    print("(B) GERENCIAR PRODUTOS")
    print("(S) SAIR")
    escolha = input("\nR: ").upper()

    if escolha == 'A':
        # Loop de menu de clientes
        while True:
            os.system('cls || clear')
            print("""
===== GERENCIADOR DE CLIENTES =====
1 - ADICIONAR
2 - MOSTRAR TODOS
3 - ATUALIZAR
4 - EXCLUIR
0 - VOLTAR
""")
            try:
                opcao = int(input('Digite uma opção: '))
            except ValueError:
                print('\nEntrada inválida. Digite um número.')
                time.sleep(2)
                continue

            match opcao:
                case 1: adicionar_cliente(lista_clientes)
                case 2: mostrar_todos_clientes(lista_clientes)
                case 3: atualizar_cliente(lista_clientes)
                case 4: excluir_cliente(lista_clientes)
                case 0: break  # Sai do submenu
                case _: print('\nOpção inválida!')
            
            time.sleep(2)

    elif escolha == 'B':
        # Loop de menu de produtos
        while True:
            os.system('cls || clear')
            print("""
===== GERENCIADOR DE PRODUTOS =====
1 - ADICIONAR
2 - MOSTRAR TODOS
3 - ATUALIZAR
4 - EXCLUIR
0 - VOLTAR
""")
            try:
                opcao = int(input('Digite uma opção: '))
            except ValueError:
                print('\nEntrada inválida. Digite um número.')
                time.sleep(2)
                continue

            match opcao:
                case 1: adicionar_produto(lista_produtos)
                case 2: mostrar_todos_produtos(lista_produtos)
                case 3: atualizar_produto(lista_produtos)
                case 4: excluir_produto(lista_produtos)
                case 0: break  # Sai do submenu
                case _: print('\nOpção inválida!')
            
            time.sleep(2)

    elif escolha == 'S':
        print('\nSaindo do programa...')
        break  # Sai do loop principal

    else:
        print('\nOpção inválida!')
        time.sleep(2)


