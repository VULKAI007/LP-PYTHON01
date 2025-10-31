import os
os.system('cls')

from dataclasses import dataclass

@dataclass
class Autor:
    nome : str
    biografia: str

@dataclass
class Livro:
    titulo: str
    ano: int
    autor: Autor

    def exibir_detalhes(self):
        print("======= DETALHES DO LIVRO =======")
        print(f"TÍTULO: {self.titulo}")
        print(f"ANO DE PUBLICAÇÃO: {self.ano}")
        print(f"AUTOR: {self.autor.nome}")

print("===== CADASTRO DE LIVRO =====")
livro1 = Livro(titulo=input("TITULO DO LIVRO: "),
                ano=input("INFORME O ANO DE LANÇAMENTO: "),
                autor= Autor(input("INFORME O NOME DO AUTOR: "),
                             biografia=input("INFORME A BIOGRAFIA DO AUTOR: ")))

os.system('cls')
livro1.exibir_detalhes()
