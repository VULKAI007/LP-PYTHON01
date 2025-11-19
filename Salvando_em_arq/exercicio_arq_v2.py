import os
os.system('cls')

from dataclasses import dataclass

@dataclass
class Funcionario:
    nome: str
    data_nascimento: str
    rg: str
    cpf: str

# 2. FUNÇÃO PARA SALVAR NO ARQUIVO
def salvar_funcionarios(lista_funcionarios, nome_arquivo):
    print(f"Salvar dados em {nome_arquivo}...")
    
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        for func in lista_funcionarios:
            
            linha = f"{func.nome},{func.data_nascimento},{func.rg},{func.cpf}\n"
            arquivo.write(linha)
    print("Dados salvos com sucesso!\n")

def ler_funcionarios(nome_arquivo):
    print(f"LER DADOS DO ARQUIVO {nome_arquivo}....")
    try:
        