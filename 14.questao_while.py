import os
os.system("cls")

c_notas = []
cont = 0


while True:

    print("===== CADERNO DE NOTAS =====")
    nota = float(input(f"INFORME A {cont + 1} NOTA QUE DESEJA REGISTAR NO SISTEMA: "))
    c_notas.append(nota)
    cont += 1
    giro = input("""DIGITE:
     (S) PARA INSERIR MASI NOTAS
     (N) PARA ENCERAR O REGISTRO
     \
     R: """).upper().strip()
    os.system('cls')
    match giro:
        case "N":
            break
        case _:
            print("INFORME UMA OPÇÃO VÁLIDA!")
            print("TENTANDO NOVAMENTE...")
            

media = sum(c_notas) / cont

if not c_notas:
    print("NENHUM NOTA FOI INFORMADA")
else:
    print(f"MEDIA DAS NOTAS INFORMADAS {media}")





