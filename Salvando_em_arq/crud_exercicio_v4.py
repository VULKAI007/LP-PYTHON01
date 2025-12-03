import os
import time
from dataclasses import dataclass

os.system('cls || clear')  # Limpar terminal

lista_alunos = []

@dataclass
class Endereco:
    logradouro: str
    numero: int
    cidade: str
    estado: str


@dataclass
class Aluno:
    nome: str
    nascimento: str
    ra: str
    curso: str
    endereco : Endereco

    def mostrar_dados(self):
        print("===== EXIBINDO DADOS DOS FUNCIONÁRIOS =====")
        print(f'\nNome: {self.nome}')
        print(f'Data de Nascimento: {self.nascimento}')
        print(f'CPF: {self.ra}')
        print(f'Função: {self.curso}')
        print(f"------ ENDEREÇO ------")
        print(f"LOGRADOURO: {self.endereco.logradouro}")
        print(f"NÚMERO: {self.endereco.numero}")
        print(f"CIDADE: {self.endereco.cidade}")
        print(f"ESTADO: {self.endereco.estado}")

    # FUNÇÃO PARA VERIFICAR SE A LISTA ESTA VÁZIA.
    def lista_esta_vazia(lista_alunos):
        if not lista_alunos:
            print("\nMÃO HÁ ALUNOS CADASTRADOS")
            return True
        return False
    
    # FUNÇÃO PARA ADICONAR UM NOVO aluno
    def adicionar_aluno(lista_aluno):
        print("\n====== ADICIONAR NOVO ALUNO ======")
        nome = input("DIGITE SEU NOME: ")
        nascimento = input("DIGITE SUA DATA DE NASCIMENTO ")
        ra = input("DIGITE SEU R.A.: ")
        curso = input("DIGITE SEU CURSO: ")
        print("------- ENDEREÇO -------")
        logradouro = input("DIGITE SEU LOGRADOURO: ")
        numero = input("DIGITE SEU NÚMERO: ")
        cidade = input("DIGITE SUA CIDADE: ")
        estado = input("DIGITE SEU ESTADO: ")

        novo_aluno = Aluno(nome=nome,
                           nascimento=nascimento,
                           ra=ra,
                           curso=curso,
                           endereco=Endereco(
                               logradouro=logradouro,
                               numero=numero,
                               cidade=cidade,
                               estado=estado
                           ))
        lista_aluno.append(novo_aluno)
        print(f"\ALUNO {nome} ADICIONADO COM SUCESSO!")

    # FUNCÃO PARA ENCONTRAR UM aluno NA LISTA.
    def encontrar_aluno_por_nome(lista_alunos, nome_buscar):
        nome_buscar_lower = nome_buscar.lower()
        for aluno in lista_alunos:
            if aluno.nome.lower() == nome_buscar_lower:
                return aluno
            return None # NONE SIGNIFICA RETONRAR VAZIO, SEN CONTEÚDO.
        
        # FUNÇÃO PARA MOSTRAR TODOS OS alunoS
    def mostrar_todos_clientes(lista_aluno):
        if lista_esta_vazia(lista_aluno):
            return
        print("\n======= LISTA DE CLIENTES ======")
        for aluno in lista_aluno:
            aluno.mostrar_dados()

    def atualizar_cliente(lista_alunos):
        if lista_esta_vazia(lista_alunos):
            return
        
        # MOSTRA A LSITA  PARA AJUDAR O USUÁRIO.
        mostrar_todos_alunos(lista_alunos)
        print("------ ATUALIZAR DADOS DO CLIENTE ------")
        nome_buscar = input("\nDIGITE O NOME DO CLIENTE: ")
        aluno_para_atualizar = encontrar_aluno_por_nome(lista_alunos, nome_buscar)

        if aluno_para_atualizar:
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

