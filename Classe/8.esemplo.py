import os
os.system('cls')

# TEXTO  QUE DESEJA SALVAR.
texto = input("DIGITE UM TEXTO: ")

# DEFINIR NOME DO ARQUIVO PARA SALVAR.
nome_arquivo = "exemplo.txt"

# COMANDO PARA SALVAR.
with open(nome_arquivo, "a") as meu_arquivo:
    meu_arquivo.write(f"{texto}\n")
    print("SALVO COM SUCESSO")