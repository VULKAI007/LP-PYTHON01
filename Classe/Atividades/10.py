import os
os.system('cls')

from dataclasses import dataclass

@dataclass
class Livro:
    titulo: str
    autor: str
    categoria: str
    preco: float

QUANTIDADE_LIVROS = 1
lista_livro = []

print("SOLICITANDO DADOS DO LIVRO. ")
for i in range(QUANTIDADE_LIVROS):
    print("===== CADASTRO DE LIVRO =====")
    livros = Livro(
        titulo=input("DIGITE O TÍTULO: "),
        autor=input("DIGITE O AUTOR: "),
        categoria= input("DIGITE A CATEGORIA: "),
        preco= float(input("DIGITE O PREÇO: "))
    )
    lista_livro.append(livros)

print()
print("SALVANDO DADOS....")
arquivo = "DADOS_LIVRO.TXT"

os.system('cls')
with open (arquivo, "a") as arquivos_livros:
    for livros in lista_livro:
        arquivos_livros.write(f"TÍTULO: {livros.titulo}\nAUTOR: {livros.autor}\nCATEGORIA: {livros.categoria}\nPREÇO: {livros.preco}")
    print("salvo com sucesso........")
      
