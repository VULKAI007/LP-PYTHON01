import os
os.system("cls")

c_notas = []
contador = 0


while True:

    print("===== CADERNO DE NOTAS =====")
    nota = float(input(f"INFORME A {contador + 1} NOTA QUE DESEJA REGISTAR NO SISTEMA: "))
    contador += 1
    if nota < 0:
        contador -= 1
        break
    else:
        c_notas.append(nota)
    
media = sum(c_notas) / contador

if not c_notas:
    print("NENHUM NOTA FOI INFORMADA")
else:
    print(f"MEDIA DAS NOTAS INFORMADAS {media:.2f}")
