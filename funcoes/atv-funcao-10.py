# ESCREVA UM PROGRAMA QUE PERMITA LER 3 NOTAS DE UMA LUNO, USANDO LAÇO DE REPETIÇÃO E INFORME
# POR MEIO DE UMA FUNÇÃO


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
    print("===== resultado =====")
    print(f"MEDIA: {media}")

# LAÇO DE EPETIÇÃO PARA CAPTAR AS NOTAS
for i in range(3):
    n= float(input(f"DIGITE A {i + 1}º NOTA: "))
    notas += n



media = calcular_media(notas)

resultado(media)