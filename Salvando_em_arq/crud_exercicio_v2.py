import os
import time 
from dataclasses import dataclass
os.system("cls || clear") # Limpa o terminal em windows e Linux.

lista_clientes = []

@dataclass
class Cliente:
    # Atributos da Classe.
    # Atributo são variáveis que pertecem à classe.
    nome: str
    email: str
    telefone: str

    # MÉTODOS PARA MOSTAR AS INFORMAÇÕES DOS CLIENTES
    # MÉTODO É O NOME DADO A UMA FUNÇÃI QUE PERTECE À CLASSE.
    def mostrar_dados(self):
        print(f"NOME: {self.nome} \nE-MAIL: {self.email} \nTELEFONE: {self.telefone}")

# FUNÇÃO PARA VERIFICAR SE A LISTA ESTA VÁZIA.
def lista_esta_vazia(lista_clientes):
    if not lista_clientes:
        print("\nNÃO HÁ CLIENTES CADASTRADOS.")
        return True
    return False

# FUNÇÃO PARA ADICONAR UM NOVO CLIENTE
def adicionar_cliente(lista_clientes):
    print("\n====== ADICIONAR NOVO CLIENTE ======")
    nome = input("DIGITE SEU NOME: ")
    email = input("DIGITE SEU E-MAIL: ")
    telefone = input("DIGITE SEU TELEFONE: ")

    novo_cliente = Cliente(nome=nome, email=email, telefone=telefone)
    lista_clientes.append(novo_cliente)
    print(f"\nCLIENTE {nome} ADICIONADO COM SUCESSO!")

# FUNCÃO PARA ENCONTRAR UM CLIENTE NA LISTA.
def encontrar_cliente_por_nome(lista_clientes, nome_buscar):
    nome_buscar_lower = nome_buscar.lower()
    for cliente in lista_clientes:
        if cliente.nome.lower() == nome_buscar_lower:
            return cliente
        return None # NONE SIGNIFICA RETONRAR VAZIO, SEN CONTEÚDO.

# FUNÇÃO PARA MOSTRAR TODOS OS CLIENTES
def mostrar_todos_clientes(lista_clientes):
    if lista_esta_vazia(lista_clientes):
        return
    print("\n======= LISTA DE CLIENTES ======")
    for cliente in lista_clientes:
        cliente.mostrar_dados()

# FUNÇÃO PARA ATUALIZAR CLIENTES 
def atualzar_cliente(lista_clientes):
    if lista_esta_vazia(lista_clientes):
        return
    
    #MOSTRAR A LISTA PARA AJUDAR O USUÁRIO.
    mostrar_todos_clientes(lista_clientes)
    print("------ ATUALIZAR DADOS DO CLIENTE ------")
    nome_buscar = input("\nDIGITE O NOME DO CLIENTE: ")
    cliente_para_atualizar = encontrar_cliente_por_nome(lista_clientes, nome_buscar)

    if cliente_para_atualizar:
        print("\nPESSOA ENCONTRADA. ")
        print("\nDIGITE OS NOVOS DADOS OU DEIXEW EM BRANCO PARA MANTER O VALOR ATUAL.")


        print("NOME ATUAL: {cliente_para_atualizar.nome}")
        novo_nome = input("NOVO NOME: ()")

        print("E-MAIL ATUAL: {cliente_para_atualizar.email}")
        novo_email = input("NOVO EMAIL: ()")

        print("E-MAIL TELEFONE: {cliente_para_atualizar.telefone}")
        novo_telefone = input("NOVO TELEFONE: ()")

        if novo_nome:
            cliente_para_atualizar.nome = novo_nome
        if novo_nome:
            cliente_para_atualizar.email = novo_email
        if novo_nome:
            cliente_para_atualizar.telefone = novo_telefone
        
        print(f"\nDADOS DO CLIENTE: {nome_buscar} ATUALIZADOS COM SUCESSO!")
    else:
        print(f"\nDADOS DO CLIENTE: {nome_buscar} NÃO ENCONTRADOS.")

def excluir_clientes(lista_clientes):
    if lista_esta_vazia(lista_clientes):
        return
    
    mostrar_todos_clientes(lista_clientes)

    nome_buscar = input("\nDIGITE O NOME DO CLIENTE QUE DESEJA EXCLUIR: ")
    
    cliente_para_remover = encontrar_cliente_por_nome(lista_clientes, nome_buscar)

    if cliente_para_remover:
        lista_clientes.remove(cliente_para_remover)
        print(f"\nCLIENTE {cliente_para_remover.nome} EXCLUÍDO COM SUCESSO!")
    else:
        print(f"CLIENTE COM O NOME {nome_buscar} NÃO ENCONTRADO. ")

# MOSTRANDO MENU:

while True:
    print("""
========= GERENCIADOR DE CLIENTES ==========
1 - ADICIONAR
2 - MOSTRAR TODOS
3 - ATUALIZAR
4 - EXCLUIR
0 - SAIR
                    
""")
    
    # EVITANDO ERROS NO PROGRAMA.
    # CASO O USUÁRIO DIGITE LETRARS.
    try:
        opcao = int(input("DIGITE UMA DAS OPÇÕES ACIMA: "))
    except ValueError:
        print("\nENTRADA INVÁLIDA. DIGITE UM NÚMERO...")
        time.sleep(3)
        os.system("cls || clear ")
        continue

    match opcao:
        case 1:
            adicionar_cliente(lista_clientes)
        case 2:
            mostrar_todos_clientes(lista_clientes)
        case 3:
            atualzar_cliente(lista_clientes)
        case 4:
            excluir_clientes(lista_clientes)
        case 0:
            print("\nSAINDO DO PROGRAMA.....")
            break
        case _:
            print("\nOPÇÃO INVÁLIDA. \nTENTE NOVAMENTE.")

    if opcao != 1 and opcao != 0:
        time.sleep(2)
    elif opcao == 1:
        time.sleep(1)

    if opcao != 0:
        os.system("cls || clear")

    
