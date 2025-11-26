import os
import time
os.system('cls')

from dataclasses import dataclass

@dataclass
class Funcionario:
    nome:str
    data_de_admissao: str
    matricula: int
    endereco: str

    def exibir_dados(self):
        print("======= DADOS DO FUNCIONÁRIO =====")
        print(f"NOME: {self.nome}, DATA DE ADMISSÃO: {self.data_de_admissao}, MATRÍCULA: {self.matricula}, ENDEREÇO: {self.endereco}\n")

@dataclass
class Cliente:
    nome: str
    data_de_nascimento: str
    endereco: str

    def exibir_dados_cliente(self):
        print("===== DADOS DO CLIENTE =====")
        print(f"NOME: {self.nome}, DATA DE NASCIMENTO: {self.data_de_nascimento}, ENDEREÇO: {self.endereco}\n")

cod_matricula = 0
lista_funcionario = []
lista_cliente = []

while True:
    print("======= CADASTRO GERAL =======")
    print("(A)FUNCIONÁRIO")
    print("(B)CLIENTE")
    print("==============================")
    print("\n")
    opcao = input("R:").upper()



    match opcao:
        case "A":
            if len(lista_funcionario) < 3:
                cod_matricula += 1
                print('---- CADASTRO DE FUNCIONÁRIO ----')
                funcionario = Funcionario(nome=input("DIGITE SEU NOME: "),
                                        data_de_admissao=input("DIGITE A DATA DE ADMISSÃO: "),
                                        matricula=cod_matricula,
                                        endereco=input("DIGITE SEU ENDEREÇO: "))
                lista_funcionario.append(funcionario)

                #ADICIONANDO O DADOS AO ARQUIVO
                nome_arquivo_funcionario = 'dados_funcionarios.csv'
                with open(nome_arquivo_funcionario, 'a') as arquivo_funcionario:
                   # for funcionario in lista_funcionario:
                    arquivo_funcionario.write(f"{funcionario.nome}, {funcionario.data_de_admissao}, {funcionario.matricula}, {funcionario.endereco}\n")
                print("DADOS SALVOS COM SUCESSO!")
                print('\n')

            else:
                print("MÁXIMO DE FUNCIONÁRIOS CADASTRADOS....")
                time.sleep(0.5)
        case "B":
            if len(lista_cliente) < 3:
                print('----- CADASTRO DE CLIENTE -----')
                cliente = Cliente(nome=input("DIGITE O SEU NOME: "),
                                  data_de_nascimento=input("DIGITE SUA DATA DE NASCIMENTO: "),
                                  endereco=input("DIGITE SEU ENDEREÇO: "))
                lista_cliente.append(cliente)

                #ADICIONANDO O DADOS AO ARQUIVO
                nome_arquivo_cliente = 'dados_cliente.csv'
                with open(nome_arquivo_cliente, 'a') as arquivo_cliente:
                    #for cliente in lista_cliente:
                    arquivo_cliente.write(f"{cliente.nome}, {cliente.data_de_nascimento}, {cliente.endereco}\n")

                    print("DADOS SALVOS COM SUCESSO!")
                    print('\n')
                
            else:
                print("MÁXIMO DE CLIENTES CADASTRADOS.....")
                time.sleep(0.5)
                print("\n")

    if len(lista_funcionario) == 3 and len(lista_cliente) == 3:
        print("FUNCIONÁRIOS E CLIENTES CADASTRADOS COM SUCESSO!!")
        print("ENCERRANDO O PROGRAMA.....")
        time.sleep(0.5)
        print('\n')

        print("====== EXIBINDO DADOS DOS FUNCIONÁRIOS ======")
        lista_geral_funcionario = []

        try:
            with open(nome_arquivo_funcionario, 'r', encoding='utf-8') as arquivo:
                #RECEBE TODOS OS DADOS DO ARQUIVO DE UMA SÓ VEZ
                lista_todos_funcionarios = arquivo.readlines()
                for funcionario in lista_todos_funcionarios:
                    nome, data_de_admissao, matricula, endereco = funcionario.strip().split(",")
                    dados_funcionario = Funcionario(nome=nome, data_de_admissao=data_de_admissao, matricula=int(matricula), endereco=endereco)
                    lista_geral_funcionario.append(dados_funcionario)
            for funcionario in lista_geral_funcionario:
                funcionario.exibir_dados()
        except FileNotFoundError:

            print("O ARQUIVO NÃO FOI ENCONTRADO. ")

        print("===== EXIBINDO DADOS DOS CLIENTES =====")
        lista_geral_cliente = []

        try:
            with open(nome_arquivo_cliente, "r", encoding="utf-8") as arquivo_cl:
                #RECEBE TODOS OS DADOS DO ARQUIVO DE UMA SÓ VEZ

                lista_todos_clientes = arquivo_cl.readlines()
                for cliente in lista_todos_clientes:
                    nome, data_de_nascimento, endereco = cliente.strip().split(",")
                    dados_cliente = Cliente(nome=nome, data_de_nascimento=data_de_nascimento, endereco=endereco)
                    lista_geral_cliente.append(dados_cliente)
            for cliente in lista_geral_cliente:
                cliente.exibir_dados_cliente()
        except FileNotFoundError:    
            print("O ARQUIVO NÃO FOI ENCONTRADO.")

        break
    


            
