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
    endereco: Endereco

    def mostrar_dados(self):
        print("===== EXIBINDO DADOS DOS ALUNOS =====")
        print(f'\nNome: {self.nome}')
        print(f'Data de Nascimento: {self.nascimento}')
        print(f'RA: {self.ra}')
        print(f'Curso: {self.curso}')
        print(f"------ ENDEREÇO ------")
        print(f"LOGRADOURO: {self.endereco.logradouro}")
        print(f"NÚMERO: {self.endereco.numero}")
        print(f"CIDADE: {self.endereco.cidade}")
        print(f"ESTADO: {self.endereco.estado}")


# Função para verificar se a lista está vazia
def lista_esta_vazia(lista_alunos):
    if not lista_alunos:
        print("\nNÃO HÁ ALUNOS CADASTRADOS")
        return True
    return False
# ESSE CÓDIGO É DE ENZO
# Função para adicionar um novo aluno
def adicionar_aluno(lista_alunos):
    print("\n====== ADICIONAR NOVO ALUNO ======")
    nome = input("DIGITE SEU NOME: ")
    nascimento = input("DIGITE SUA DATA DE NASCIMENTO: ")
    ra = input("DIGITE SEU R.A.: ")
    curso = input("DIGITE SEU CURSO: ")
    print("------- ENDEREÇO -------")
    logradouro = input("DIGITE SEU LOGRADOURO: ")
    numero = int(input("DIGITE SEU NÚMERO: "))
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
    lista_alunos.append(novo_aluno)
    print(f"\nALUNO {nome} ADICIONADO COM SUCESSO!")


# Função para encontrar um aluno por nome
# ESSE CÓDIGO É DE ENZO
def encontrar_aluno_por_nome(lista_alunos, nome_buscar):
    nome_buscar_lower = nome_buscar.lower()
    for aluno in lista_alunos:
        if aluno.nome.lower() == nome_buscar_lower:
            return aluno
    return None  # Retorna None se não encontrar o aluno


# Função para mostrar todos os alunos
def mostrar_todos_alunos(lista_alunos):
    if lista_esta_vazia(lista_alunos):
        return
    print("\n======= LISTA DE ALUNOS ======")
    for aluno in lista_alunos:
        aluno.mostrar_dados()


# Função para atualizar os dados de um aluno
def atualizar_aluno(lista_alunos):
    if lista_esta_vazia(lista_alunos):
        return
    
    mostrar_todos_alunos(lista_alunos)
    print("------ ATUALIZAR DADOS DO ALUNO ------")
    nome_buscar = input("\nDIGITE O NOME DO ALUNO: ")
    aluno_para_atualizar = encontrar_aluno_por_nome(lista_alunos, nome_buscar)

    if aluno_para_atualizar:
        print("\nALUNO ENCONTRADO. ")
        print("\nDIGITE OS NOVOS DADOS OU DEIXE EM BRANCO PARA MANTER O VALOR ATUAL.")

        novo_nome = input(f"NOME ATUAL: {aluno_para_atualizar.nome}\nNOVO NOME: ")
        novo_nascimento = input(f"NASCIMENTO ATUAL: {aluno_para_atualizar.nascimento}\nNOVO NASCIMENTO: ")
        novo_ra = input(f"RA ATUAL: {aluno_para_atualizar.ra}\nNOVO RA: ")
        novo_curso = input(f"CURSO ATUAL: {aluno_para_atualizar.curso}\nNOVO CURSO: ")
        
        novo_logradouro = input(f"LOGRADOURO ATUAL: {aluno_para_atualizar.endereco.logradouro}\nNOVO LOGRADOURO: ")
        novo_numero = input(f"NÚMERO ATUAL: {aluno_para_atualizar.endereco.numero}\nNOVO NÚMERO: ")
        novo_cidade = input(f"CIDADE ATUAL: {aluno_para_atualizar.endereco.cidade}\nNOVA CIDADE: ")
        novo_estado = input(f"ESTADO ATUAL: {aluno_para_atualizar.endereco.estado}\nNOVO ESTADO: ")

        if novo_nome:
            aluno_para_atualizar.nome = novo_nome
        if novo_nascimento:
            aluno_para_atualizar.nascimento = novo_nascimento
        if novo_ra:
            aluno_para_atualizar.ra = novo_ra
        if novo_curso:
            aluno_para_atualizar.curso = novo_curso
        if novo_logradouro:
            aluno_para_atualizar.endereco.logradouro = novo_logradouro
        if novo_numero:
            aluno_para_atualizar.endereco.numero = novo_numero
        if novo_cidade:
            aluno_para_atualizar.endereco.cidade = novo_cidade
        if novo_estado:
            aluno_para_atualizar.endereco.estado = novo_estado
        
        print(f"\nDADOS DO ALUNO: {nome_buscar} ATUALIZADOS COM SUCESSO!")
    else:
        print(f"\nALUNO: {nome_buscar} NÃO ENCONTRADO.")


# Função para excluir um aluno
def excluir_aluno(lista_alunos):
    if lista_esta_vazia(lista_alunos):
        return
    
    mostrar_todos_alunos(lista_alunos)
    nome_buscar = input('\nDigite o nome do aluno que deseja excluir: ')
    aluno = encontrar_aluno_por_nome(lista_alunos, nome_buscar)

    if aluno:
        lista_alunos.remove(aluno)
        print(f'\nALUNO {aluno.nome} EXCLUÍDO COM SUCESSO!')
    else:
        print('\nALUNO NÃO ENCONTRADO.')


# MENU PRINCIPAL
# ESSE CÓDIGO É DE ENZO
while True:
    print("""
---- Gerenciador de alunos ----
1 - Adicionar
2 - Mostrar todos
3 - Atualizar
4 - Excluir
0 - Sair
""")

    try:
        opcao = int(input('Digite uma opção: '))
    except ValueError:
        print('\nEntrada inválida. Digite um número.')
        time.sleep(2)
        os.system('cls || clear')
        continue

    match opcao:
        case 1:
            adicionar_aluno(lista_alunos)
        case 2:
            mostrar_todos_alunos(lista_alunos)
        case 3:
            atualizar_aluno(lista_alunos)
        case 4:
            excluir_aluno(lista_alunos)
        case 0:
            print('\nSaindo do programa...')
            break
        case _:
            print('\nOpção inválida!')

    if opcao != 0:
        time.sleep(2)
        os.system('cls || clear')
