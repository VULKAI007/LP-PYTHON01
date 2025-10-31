import os
os.system('cls')

from dataclasses import dataclass

@dataclass
class Aluno:
    nome: str
    idade: int
    telefone: str
    e_mail: str

QUANTIDADE_ALUNOS = 1
lista_alunos = []

print("SOLICITANDO DADOS DO ALUNO. ")
for i in range(QUANTIDADE_ALUNOS):
    print("===== CADASTRO DE ALUNO =====")
    aluno = Aluno(
        nome=input("DIGITE SEU NOME: "),
        idade=int(input("DIGITE SUA IDADE: ")),
        telefone= input("DIGITE SEU TELEFONE: "),
        e_mail= input("DIGITE SEU E-MAIL: ")
    )
    lista_alunos.append(aluno)
cont = 0
print()
print("SALVANDO DADOS....")
arquivo = "DADOS_ALUNOS.TXT"

os.system('cls')
with open (arquivo, "a") as arquivos_alunos:
    for aluno in lista_alunos:
        cont += 1
        arquivos_alunos.write(
            f"===== ALUNO CADASTRADO ====\nNOME: {aluno.nome}\nIDADE: {aluno.idade}\nTELEFONE: {aluno.telefone}\nE-MAIL: {aluno.e_mail}\n")
    print("SALVO COM SUCESSO!")