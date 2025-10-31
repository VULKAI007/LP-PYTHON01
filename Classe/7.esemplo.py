import os
os.system('cls')
from dataclasses import dataclass

@dataclass
class Aluno:
    nome: str
    idade: int

QUANTIDADE_ALUNOS = 2
lista_alunos = []

print("SOLICITANDO DADOS DO ALUNO. ")
for i in range(QUANTIDADE_ALUNOS):
    aluno = Aluno(
        nome=input("DIGITE SEU NOME: "),
        idade=int(input("DIGITE SUA IDADE: "))
    )
    lista_alunos.append(aluno)

print()
print("SALVANDO DADOS....")
arquivo = "DADOS_ALUNOS.TXT"

with open (arquivo, "w") as arquivos_alunos:
    for aluno in lista_alunos:
        arquivos_alunos.write(f"{aluno.nome}, {aluno.idade}\n ")
    print("SALVO COM SUCESSO!")