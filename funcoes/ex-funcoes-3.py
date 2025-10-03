import os
os.system('cls')

# FUNÇÃO COM PASSAGEM DE PARÂMETROS
# CRIANDO UMA FUNCÇÃO.

def saudacao(nome,idade, altura, peso):
    print("====== RESPOSTA ======")
    print(f"OLÁ, {nome}! BEM-VINDO(A)!")
    print(f"SUA IDADE É {idade} ANOS")
    print(f"SUA ALTURA É {altura}")
    print(f"SEU PESO É {peso}")

print("SOLICITANDO DADOS.")
nome = input("DIGITE SEU NOME: ")
idade = int(input("DIGITE SUA IDADE: "))
altura = float(input("DIGITE SUA ALTURA: "))
peso = float(input("DIGITE SEU PESO: "))

# CHAMANDO A FUNÇÃO.

saudacao(nome,idade,altura,peso)
