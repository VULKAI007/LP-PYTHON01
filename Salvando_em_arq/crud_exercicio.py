import os
import time
os.system('cls')

lista_cliente = []
while True:
    print("====== MENU DE CRUD =====")
    print("(1)CREAT")
    print("(2)READ")
    print("(3)UPDATE")
    print("(4)DELETE")
    print("(5)SAIR")
    print("===========================\n")
    opcao = int(input("r:"))

    match opcao:
        case 1:
            print("------ CADASTRO DE CLIENTE ------")
            nome = input("DIGITE UM NOME: ")
            lista_cliente.append(nome)
        case 2:
            print("------ CLIENTES CADASTRADOS ------")
            if len(lista_cliente) != 0:
                for cliente in lista_cliente:
                    print(lista_cliente)
                else:
                    print("NÃO EXISTE NENHUM CLIENTE CADASTRADO!")
                    print("REINICIANDO....")
                    time.sleep(0.5)
        case 3:
            print("------ ATUALIZAR CLIENTE -----")
            nome_para_atualizar = input("DIGITE O NOME QUE DESEJA ATUALIZAR: ")
            if nome_para_atualizar in lista_cliente:
                novo_nome = input("DIGITE O NOME ATUALIZADO: ")
                indice = lista_cliente.index(nome_para_atualizar)
                lista_cliente[indice] = novo_nome
                print(f"O NOME {nome_para_atualizar} FOI ATUALIZADO PARA {novo_nome}")
            else:
                print(f"O NOME {nome_para_atualizar} NÃO FOI ENCONTRADO. ")
        case 4:
            print("----- DELETANDO DADOS -----")
            nome_para_excluir = input("DIGITE O NOME QUE DESEJA EXCLUIR: ")
            if nome_para_excluir in lista_cliente:
                lista_cliente.remove(nome_para_excluir)
                print(f"O NOME {nome_para_excluir} FOI EXCLUÍDO COM SUCESSO!")
            else:
                print(f"O NOME {nome_para_excluir}  NÃO FOI ENCONTRADO. ")
        case 5:
            break
        case _:
            print("DIGITE UMA OPÇÃO VÁLIDA....")
            time.sleep(1)
