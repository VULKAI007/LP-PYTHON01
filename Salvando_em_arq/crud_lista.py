import os
os.system('cls')

# CRUD usando lista.
# Create = Criar / salvar
# Read =  buscar / selecionar
# Uptade = atualizar / selecionar
# Delete = excluir

# Criando uma lista.
lista_clientes = []
print("CREATE - Adicionar / Inserir")
nome = "MARTA"
lista_clientes.append(nome)
print(f"O NOME: {nome} FOI INSERIDO COM SUCESSO! ")

# READ
print("\nREAD - LER / MOSTRAR ")
print(lista_clientes)

# UPDATE
print("\nUPDATE - ATUALZAR / ALTERAR")
nome_para_atualizar = "MARTA"
if nome_para_atualizar in lista_clientes:
    novo_nome = "MARTA SILVA"
    indice = lista_clientes.index(nome_para_atualizar)
    lista_clientes[indice] = novo_nome
    print(f"O NOME {nome_para_atualizar} FOI ATUALIZADO PARA {novo_nome}")
else:
    print(f"O NOME {nome_para_atualizar} NÃO FOI ENCONTRADO. ")

print(lista_clientes)

# DELETE
print("\nDELETE = EXCLUIR / REMOVER")
nome_para_excluir = "MARIA"
if nome_para_excluir in lista_clientes:
    lista_clientes.remove(nome_para_excluir)
    print(f"O NOME {nome_para_excluir} FOI EXCLUÍDO COM SUCESSO!")
else:
    print(f"O NOME {nome_para_excluir}  NÃO FOI ENCONTRADO. ")

print(lista_clientes)