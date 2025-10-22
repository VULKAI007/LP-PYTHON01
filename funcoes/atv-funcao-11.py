# ESCREVA UM PRGRAMA QUE PERMITA LER 2 NOTAS DE UM ALUNO E INFROME POR MEIO DE FUNÇÕES:
# A MÉDIA; COM BASE NA MÉDIA SE ALUNO FOI APROVADO OU REPROVADO
# CRITÉRIO PAR APROVAÃO: MÉDIA 7,0

import os
os.system('cls')
n = 0
notas= 0

# FUNCÇÃO PARA CALCULAR A MÉDIA
def calcular_media(n1):
    calcular = n1 / 3
    return calcular

#FUNÇÃO PARA MOSTRAR O RESULTADO
def resultado(media):
    print("===== RESULTADO =====")
    if media >= 7:
        print(f"MEDIA: {media}")
        print("ALUNO APROVADO")
    else:
        print(f"MÉDIA: {media}")
        print("ALUNO REPROVADO")


# LAÇO DE EPETIÇÃO PARA CAPTAR AS NOTAS
for i in range(3):
    while True:
        n= float(input(f"DIGITE A {i + 1}º NOTA: "))
        if n >= 0 and n <= 10:
            notas += n
            break
        else:
            print("INFORME UMA NOTA VÁLIDA! TENTE NOVAMENTE")


media = calcular_media(notas)

resultado(media)